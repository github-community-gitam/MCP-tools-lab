from mcp_tools_lab.tools.diff import compare_text


def test_replacement():
    result = compare_text("hello\nold", "hello\nnew\nextra")
    assert result["unchanged_lines"]==1
    assert result["added_lines"] == 2
    assert result["removed_lines"] == 1
    assert "-old" in result["diff"]
    assert "+new" in result["diff"]


def test_equal_empty_and_newlines():
    assert compare_text("", "")["unchanged_lines"] == 0
    assert compare_text("", "")["diff"] == ""
    assert compare_text("same\r\n", "same")["diff"] == ""
    assert compare_text("", "new")["added_lines"] == 1
    assert compare_text("old", "")["removed_lines"] == 1
