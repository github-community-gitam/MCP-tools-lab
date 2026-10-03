# Contributing to MCP Tools Lab

Welcome! Your first contribution can be a small Python change. You do not need
experience with MCP, AI, or every tool in this repository.

## Understand the repository

MCP Tools Lab is a community hackathon project with seven local developer tools
exposed through one Python MCP server. The tools analyze text, process JSON,
inspect CSV, generate hashes, compare text, convert timestamps, and parse URLs.
They require no API keys or AI models and make no network requests.

Read [README.md](https://github.com/github-community-gitam/MCP-tools-lab/blob/main/README.md) for installation and usage, and
[docs/tool-guide.md](https://github.com/github-community-gitam/MCP-tools-lab/blob/main/docs/tool-guide.md) for each tool's behavior.

```text
src/mcp_tools_lab/server.py  # Registers all seven functions with MCP
src/mcp_tools_lab/tools/     # Independent Python functions you can edit
tests/                      # Tool tests and an MCP round-trip test
examples/try_tools.py       # Try every tool without an MCP client
docs/tool-guide.md          # Input/output documentation to keep up to date
docs/issues/                # Six starter task briefs
```

## 1. Pick one task

Read the [six starter tasks](https://github.com/github-community-gitam/MCP-tools-lab/blob/main/docs/issues/README.md) or the
[open GitHub issues](https://github.com/github-community-gitam/MCP-tools-lab/issues).
Choose one issue, check whether someone is already working on it, and comment
that you would like to try it. Ask questions when a requirement is unclear.
Wait for a maintainer to confirm if the issue is already claimed.

The empty-line counter and uppercase hash option are good starting points.
CSV previews and millisecond conversion offer a slightly bigger challenge.

Six optional enhancements are left for contributors:

- [Count empty lines in Text Analyzer](https://github.com/github-community-gitam/MCP-tools-lab/blob/main/docs/issues/01-empty-lines.md).
- [Choose 2-space or 4-space JSON indentation](https://github.com/github-community-gitam/MCP-tools-lab/blob/main/docs/issues/02-json-indentation.md).
- [Add an uppercase hash option](https://github.com/github-community-gitam/MCP-tools-lab/blob/main/docs/issues/03-uppercase-hashes.md).
- [Preview the first few CSV data rows](https://github.com/github-community-gitam/MCP-tools-lab/blob/main/docs/issues/04-csv-preview.md).
- [Count unchanged lines in Text Comparison](https://github.com/github-community-gitam/MCP-tools-lab/blob/main/docs/issues/05-unchanged-lines.md).
- [Support Unix milliseconds in Timestamp Converter](https://github.com/github-community-gitam/MCP-tools-lab/blob/main/docs/issues/06-milliseconds.md).

All seven tools already work without these enhancements. Each issue brief includes
examples, the exact function to edit, acceptance criteria, and a focused test command.

## 2. Fork and clone

Click **Fork** on GitHub to make your own copy. Replace YOUR-USERNAME below:

```sh
git clone https://github.com/YOUR-USERNAME/MCP-tools-lab.git
cd MCP-tools-lab
git switch -c add-empty-line-count
python -m venv .venv
```

Activate the environment with `.venv\Scripts\Activate.ps1` on Windows PowerShell
or `source .venv/bin/activate` on macOS/Linux. If activation is blocked on Windows,
use `.venv\Scripts\python.exe` in place of `python` in the remaining commands.

```sh
python -m pip install -e ".[dev]"
python -m pytest -q
```

Run the tests before editing so you know the initial setup works.
The editable installation (`-e`) means changes under `src/` take effect immediately.
You can also run `python examples/try_tools.py` to see every tool in action.

## 3. Make a small change

Each tool lives in `src/mcp_tools_lab/tools/`. Its corresponding tests live in
`tests/`. For example, Text Analyzer is in `tools/text.py`, with tests in
`tests/test_text.py`. The issue names the exact function to edit.

Tool functions take normal Python arguments and return dictionaries. The server
registers these functions automatically, so an optional parameter with a type
annotation becomes available to MCP clients without another wrapper.

- Keep the change focused on your issue.
- Use descriptive names, type annotations, and a short docstring.
- Preserve existing behavior unless your issue explicitly changes it.
- Give new optional parameters defaults so existing calls keep working.
- Use Python's standard library for tool logic. Do not add keys, models, or network calls.
- Avoid printing inside tool functions: standard output carries MCP messages.
- Update `docs/tool-guide.md` when you change inputs or outputs.

## 4. Add and run tests

A test is a small function that checks expected behavior using `assert`:

```python
from mcp_tools_lab.tools.text import analyze_text

def test_two_words():
    result = analyze_text("hello world")
    assert result["words"] == 2
```

Test one normal example and relevant edge cases, such as empty input. Keep existing
tests passing. Run a focused test file while working, then the complete suite:

```sh
python -m pytest tests/test_text.py -q
python -m pytest -q
```

`tests/test_server.py` starts the real MCP server as a child process and checks
discovery and calls. You do not need a separate MCP application to run it.

## 5. Open a pull request

Review your changes, stage only the files you intended to change, and push:

```sh
git diff
git add src/mcp_tools_lab/tools/text.py tests/test_text.py docs/tool-guide.md
git commit -m "Add empty-line count to text analyzer"
git push -u origin add-empty-line-count
```

Replace the sample paths and branch name with those for your issue. On GitHub,
open a pull request from your branch to the original repository's `main` branch.
Explain what changed, include your test result, and write `Closes #NUMBER` using
the real issue number. A draft pull request is welcome if you need help.

Never commit `.venv`, credentials, or generated cache files. These are ignored by
the project. Maintainers will review your work and may suggest small adjustments.
Please keep discussion patient and respectful; see the [Code of Conduct](https://github.com/github-community-gitam/MCP-tools-lab/blob/main/CODE_OF_CONDUCT.md).
