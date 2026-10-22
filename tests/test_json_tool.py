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
def test_default_indent_is_two_spaces():
    assert process_json('{"a":1}')["output"] == '{\n  "a": 1\n}'
    assert process_json('{"a":1}', indent=2)["output"] == '{\n  "a": 1\n}'
def test_indent_four():
    assert process_json('{"a":1}', indent=4)["output"] == '{\n    "a": 1\n}'
def test_nested_indent():
    result = process_json('{"outer":{"inner":1}}', indent=4)
    assert result["output"] == '{\n    "outer": {\n        "inner": 1\n    }\n}'
    result = process_json('{"outer":{"inner":1}}')
    assert result["output"] == '{\n  "outer": {\n    "inner": 1\n  }\n}'
def test_indent_is_validated_for_every_action():
    with pytest.raises(ValueError, match="indent"):
        process_json("{}", "minify", indent=3)
    with pytest.raises(ValueError, match="indent"):
        process_json("{}", "validate", indent=0)
    with pytest.raises(ValueError, match="indent"):
        process_json("{}", indent=-2)
    # Valid indent keeps existing minify and validate behavior unchanged.
    assert process_json('{"a":1}', "minify", indent=4)["output"] == '{"a":1}'
    assert process_json('{"a":1}', "validate", indent=4) == {"valid": True}
