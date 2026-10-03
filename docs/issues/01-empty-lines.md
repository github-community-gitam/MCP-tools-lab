# Count empty lines in Text Analyzer

**Level:** Beginner · **Suggested labels:** `good first issue`, `enhancement`

## What to build

Text Analyzer counts all lines but does not say how many are blank. Add an
`empty_lines` field to its result. A line is empty when it contains no characters
or only whitespace, such as spaces or tabs.

## Where to work

- Function: `analyze_text` in `src/mcp_tools_lab/tools/text.py`
- Tests: `tests/test_text.py`
- Documentation: `docs/tool-guide.md`

## Example

For `"hello\n\n   \nworld"`, the new `empty_lines` value should be `2`.
The existing output fields must retain their current values.

## Acceptance checklist

- [ ] Add `empty_lines` to every successful result.
- [ ] Empty input returns `0`.
- [ ] Spaces-only and tabs-only lines count as empty.
- [ ] Follow the existing `splitlines()` behavior: `"hello\n"` has zero empty lines.
- [ ] Update the exact-output assertion for empty text and add focused tests.
- [ ] Document the new field.

**Hint:** Try `line.strip()` on a line containing spaces. You can count with a loop.

Run `python -m pytest tests/test_text.py -q`, then `python -m pytest -q`.
No changes to the MCP server are needed.
