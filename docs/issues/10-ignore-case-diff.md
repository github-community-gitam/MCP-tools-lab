# Add case-insensitive text comparison

**Level:** Intermediate · **Suggested labels:** `help wanted`, `enhancement`

## What to build

Add `ignore_case: bool = False` to `compare_text`. When enabled, compare lines
using `str.casefold()` so differences in letter case alone are ignored.

## Where to work

- Function: `compare_text` in `src/mcp_tools_lab/tools/diff.py`
- Tests: `tests/test_diff.py`
- Documentation: `docs/tool-guide.md`

## Examples

- Comparing `"Hello"` and `"hello"` with `ignore_case=True` returns zero added/removed lines and an empty diff.
- Comparing `"Hello\nOLD"` and `"hello\nNEW"` returns one added and one removed line.

## Acceptance checklist

- [ ] Default calls preserve the existing result and diff format exactly.
- [ ] When enabled, use casefolded lines for both counts and unified diff generation.
- [ ] Display the casefolded text in the optional mode's diff; document this explicitly.
- [ ] Keep whitespace significant and retain the existing line-ending/final-newline rules.
- [ ] Test case-only changes, real changes mixed with case changes, empty input, and Unicode such as `Straße` versus `STRASSE`.
- [ ] If `unchanged_lines` has been added, calculate it using the same comparison mode.
- [ ] Add tests and document the option and its displayed-text behavior.

**Hint:** Build the line lists as usual, then optionally casefold each line before
passing the lists to the existing comparison code. No new diff algorithm is needed.

Run `python -m pytest tests/test_diff.py -q`, then `python -m pytest -q`.
