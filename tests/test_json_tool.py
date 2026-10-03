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
