import pytest

from mcp_tools_lab.tools.json_tool import process_json


def test_format_minify_and_sort():
    assert process_json('{"b":2,"a":1}', sort_keys=True)["output"] == '{\n  "a": 1,\n  "b": 2\n}'
    assert process_json(' { "a": [1, 2] } ', "minify")["output"] == '{"a":[1,2]}'


@pytest.mark.parametrize("text", ['{"a":}', 'NaN', 'Infinity', '{', '1e9999'])
def test_invalid_or_unsupported_json(text):
    result = process_json(text)
    assert result["valid"] is False
    assert result["error"]


@pytest.mark.parametrize("text", ['null', '[]', 'true', '"hello"', '42'])
def test_scalar_and_container_validation(text):
    assert process_json(text, "validate") == {"valid": True}


def test_unknown_action():
    with pytest.raises(ValueError, match="action"):
        process_json("{}", "unknown")


def test_format_default_indent():
    result = process_json('{"a": {"b": 1}}')
    assert result["valid"] is True
    assert result["output"] == '{\n  "a": {\n    "b": 1\n  }\n}'


def test_format_with_four_space_indent():
    result = process_json('{"a": {"b": 1}}', indent=4)
    assert result["valid"] is True
    assert result["output"] == '{\n    "a": {\n        "b": 1\n    }\n}'


@pytest.mark.parametrize("action", ["validate", "format", "minify"])
def test_unsupported_indent(action):
    with pytest.raises(ValueError, match="indent must be 2 or 4"):
        process_json("{}", action=action, indent=3)