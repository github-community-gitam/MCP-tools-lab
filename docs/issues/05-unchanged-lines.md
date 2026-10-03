# Count unchanged lines in Text Comparison

**Level:** Beginner · **Suggested labels:** `good first issue`, `enhancement`

## What to build

Text Comparison counts additions and removals. Add an `unchanged_lines` field
that counts matching lines in the alignment already produced by the function.

## Where to work

- Function: `compare_text` in `src/mcp_tools_lab/tools/diff.py`
- Tests: `tests/test_diff.py`
- Documentation: `docs/tool-guide.md`

## Example

Comparing `"hello\nold"` with `"hello\nnew"` should return
`unchanged_lines=1`, `added_lines=1`, and `removed_lines=1`.

## Acceptance checklist

- [ ] Return `unchanged_lines` alongside the existing fields.
- [ ] Identical two-line inputs return `2`; two empty inputs return `0`.
- [ ] Entirely different inputs return `0`.
- [ ] Preserve existing diff output, addition/removal counts, and newline rules.
- [ ] Include a test with repeated lines to check counting in the existing alignment.
- [ ] Document the new field.

**Hint:** In the existing loop, `tag == "equal"` marks matching sections.
The number of lines in that section is `old_end - old_start`. You do not need to
understand or replace the diff algorithm.

Run `python -m pytest tests/test_diff.py -q`, then `python -m pytest -q`.
