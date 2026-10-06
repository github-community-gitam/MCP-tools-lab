"""Regression tests for the contributor checks, using temporary source files."""

import importlib.util
from pathlib import Path

import pytest

SCRIPT = Path(__file__).resolve().parents[1] / ".github/scripts/check_rules.py"
spec = importlib.util.spec_from_file_location("check_rules", SCRIPT)
rules = importlib.util.module_from_spec(spec)
spec.loader.exec_module(rules)


@pytest.mark.parametrize("source", [
    'print("debug")',
    'import sys\nsys.stdout.write("debug")',
    'import requests',
    'from urllib import request',
    'import urllib.request',
    'import http.client',
    'def broken(:',
])
def test_blocking_source(source, tmp_path, monkeypatch):
    monkeypatch.setattr(rules, "ROOT", tmp_path)
    path = tmp_path / "tool.py"
    path.write_text(source, encoding="utf-8")
    assert rules.check_source_file(path) > 0


def test_parser_and_strings_are_allowed(tmp_path, monkeypatch):
    monkeypatch.setattr(rules, "ROOT", tmp_path)
    path = tmp_path / "tool.py"
    path.write_text('from urllib.parse import urlsplit\ntext = "print() import requests"', encoding="utf-8")
    assert rules.check_source_file(path) == 0


def test_warnings_are_nonblocking(capsys, monkeypatch):
    monkeypatch.setattr(rules, "IN_CI", False)
    assert rules.check_pr_shape([
        "src/mcp_tools_lab/tools/text.py", "src/mcp_tools_lab/tools/urls.py", "pyproject.toml",
    ]) is None
    assert capsys.readouterr().out.count("WARNING:") == 4


def test_missing_source_fails(tmp_path, monkeypatch):
    monkeypatch.setattr(rules, "SRC", tmp_path / "missing")
    assert rules.main() == 1


def test_network_submodules():
    assert rules.is_network_module("urllib.request.submodule")
    assert not rules.is_network_module("urllib.parse")
