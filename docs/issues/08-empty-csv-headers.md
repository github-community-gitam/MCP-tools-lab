# Report empty CSV column names

**Level:** Beginner–intermediate · **Suggested labels:** `help wanted`, `enhancement`

## What to build

Add `empty_header_indices` to successful CSV Inspector results so callers can
identify columns without a meaningful name. Use zero-based positions.

## Where to work

- Function: `inspect_csv` in `src/mcp_tools_lab/tools/csv_tool.py`
- Tests: `tests/test_csv_tool.py`
- Documentation: `docs/tool-guide.md`

## Example

`inspect_csv("name,,   \nAda,20,Python")` should include `empty_header_indices=[1, 2]`.

## Acceptance checklist

- [ ] Flag empty and whitespace-only header cells using `strip()`.
- [ ] Return an empty list for empty input or headers with no blank names.
- [ ] Handle header-only input and quoted empty header cells.
- [ ] Preserve original header names, missing-value counts, and all existing results.
- [ ] Blank names are a warning, not a reason to set `valid=False`.
- [ ] Malformed CSV retains its existing error response.
- [ ] Add tests and document zero-based indexing.

**Hint:** Use `enumerate(header)` to get each column's position and name.

Run `python -m pytest tests/test_csv_tool.py -q`, then `python -m pytest -q`.
