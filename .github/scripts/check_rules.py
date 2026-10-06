"""House rules for MCP Tools Lab, checked on every pull request.

Run it yourself before pushing:

    python .github/scripts/check_rules.py                 # rules only
    python .github/scripts/check_rules.py origin/main     # rules + PR-shape hints

BLOCKING (exit 1) - these break the project for everyone:
  1. print() or sys.stdout.write() inside src/. The MCP server talks to its
     client over standard output, so one stray print corrupts the protocol
     stream and the client disconnects.
  2. Network modules imported inside src/. The README promises every tool runs
     locally with no outbound requests.

WARNINGS (never fail the build) - things a reviewer will ask about:
  3. A tool module changed but nothing under tests/ did.
  4. A tool module changed but docs/tool-guide.md did not.
  5. More than one tool module changed (one issue per pull request).
  6. pyproject.toml changed (new dependencies need a maintainer's OK).

The checks use Python's ast module, so the word "print" inside a docstring or
a string is not a false positive. Only real calls and real imports count.
"""

from __future__ import annotations

import ast
import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / "src" / "mcp_tools_lab"
TOOLS_PREFIX = "src/mcp_tools_lab/tools/"

# Top-level module names that open network connections. Matching is on the
# full dotted path or its first component, so "urllib.parse" stays allowed
# (inspect_url needs it) while "urllib.request" is blocked.
NETWORK_MODULES = {
    "socket", "ssl", "requests", "httpx", "aiohttp", "urllib3", "websockets",
    "ftplib", "smtplib", "poplib", "imaplib", "telnetlib", "xmlrpc",
    "http.client", "urllib.request", "http.server", "socketserver",
}

IN_CI = os.environ.get("GITHUB_ACTIONS") == "true"


def report(level: str, path: str | None, line: int | None, message: str) -> None:
    """Print a message, as a GitHub annotation in CI so it shows on the diff."""
    if IN_CI:
        location = ""
        if path:
            location = f" file={path}" + (f",line={line}" if line else "")
        print(f"::{level}{location}::{message}")
    else:
        where = f"{path}:{line}: " if path and line else (f"{path}: " if path else "")
        print(f"{level.upper()}: {where}{message}")


def is_network_module(name: str) -> bool:
    return any(name == blocked or name.startswith(blocked + ".")
               for blocked in NETWORK_MODULES)


def check_source_file(path: Path) -> int:
    """Return the number of blocking problems found in one file."""
    rel = path.relative_to(ROOT).as_posix()
    try:
        tree = ast.parse(path.read_text(encoding="utf-8"), filename=rel)
    except SyntaxError as exc:
        report("error", rel, exc.lineno, f"Python could not parse this file: {exc.msg}")
        return 1

    problems = 0
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            func = node.func
            if isinstance(func, ast.Name) and func.id == "print":
                report("error", rel, node.lineno,
                       "print() is not allowed in src/. Standard output carries MCP "
                       "messages, so this corrupts the protocol. Return the value "
                       "in the result dict instead.")
                problems += 1
            elif (isinstance(func, ast.Attribute) and func.attr in {"write", "writelines"}
                  and isinstance(func.value, ast.Attribute) and func.value.attr == "stdout"):
                report("error", rel, node.lineno,
                       "Writing to sys.stdout is not allowed in src/ for the same "
                       "reason as print(): it corrupts the MCP message stream.")
                problems += 1
        elif isinstance(node, ast.Import):
            for alias in node.names:
                if is_network_module(alias.name):
                    report("error", rel, node.lineno,
                           f"'import {alias.name}' opens network access. Every tool "
                           "must run locally with no outbound requests.")
                    problems += 1
        elif isinstance(node, ast.ImportFrom) and node.module and node.level == 0:
            full = [node.module] + [f"{node.module}.{a.name}" for a in node.names]
            if any(is_network_module(name) for name in full):
                report("error", rel, node.lineno,
                       f"'from {node.module} import ...' opens network access. Every "
                       "tool must run locally with no outbound requests.")
                problems += 1
    return problems


def changed_files(base: str) -> list[str]:
    out = subprocess.run(
        ["git", "diff", "--name-only", "--diff-filter=ACMR", f"{base}...HEAD"],
        cwd=ROOT, capture_output=True, text=True, check=True,
    ).stdout
    return [line for line in out.splitlines() if line]


def check_pr_shape(files: list[str]) -> None:
    tools = sorted(f for f in files
                   if f.startswith(TOOLS_PREFIX) and f.endswith(".py")
                   and not f.endswith("__init__.py"))
    tests = [f for f in files if f.startswith("tests/")]

    print(f"Changed files: {len(files)}  (tool modules: {len(tools)}, test files: {len(tests)})")

    if tools and not tests:
        report("warning", tools[0], None,
               "You changed a tool but no test file. Add at least one test in "
               "tests/ that fails without your change and passes with it.")
    if tools and "docs/tool-guide.md" not in files:
        report("warning", tools[0], None,
               "You changed a tool but not docs/tool-guide.md. If the inputs or "
               "outputs changed, document them there.")
    if len(tools) > 1:
        report("warning", None, None,
               f"This pull request changes {len(tools)} tool modules "
               f"({', '.join(Path(t).name for t in tools)}). Pull requests are "
               "easiest to review when they cover one issue each.")
    if "pyproject.toml" in files:
        report("warning", "pyproject.toml", None,
               "pyproject.toml changed. Tool logic should use the standard library "
               "only, so new dependencies need a maintainer's approval.")


def main() -> int:
    files = sorted(SRC.rglob("*.py"))
    if not files:
        report("error", None, None, "No Python source files found under src/mcp_tools_lab/.")
        return 1
    problems = sum(check_source_file(f) for f in files)
    print(f"Scanned {len(files)} files under src/ for print() and network imports: "
          f"{'OK' if problems == 0 else f'{problems} problem(s)'}")

    if len(sys.argv) > 1:
        check_pr_shape(changed_files(sys.argv[1]))

    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
