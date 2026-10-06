# Count characters excluding whitespace in Text Analyzer

**Level:** Beginner · **Suggested labels:** `good first issue`, `enhancement`

## What to build

Add `characters_without_whitespace` to `analyze_text` results. Keep the existing
`characters` count, which includes whitespace.

## Where to work

- Function: `analyze_text` in `src/mcp_tools_lab/tools/text.py`
- Tests: `tests/test_text.py`
- Documentation: `docs/tool-guide.md`

## Example

`analyze_text("Hi there!\n")` should return `characters_without_whitespace=8`.

## Acceptance checklist

- [ ] Count every character except those recognized by `str.isspace()`.
- [ ] Include punctuation and digits; this is a character count, not a word count.
- [ ] Empty and whitespace-only input return zero.
- [ ] Preserve all existing fields and their values.
- [ ] Test spaces, tabs, newlines, and a Unicode non-breaking space.
- [ ] Update exact-result assertions where necessary and document the new field.

**Hint:** Loop over the text and count characters for which `character.isspace()` is false.
This task is separate from the empty-line count issue.

Run `python -m pytest tests/test_text.py -q`, then `python -m pytest -q`.
