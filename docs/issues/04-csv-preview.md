# Preview the first few CSV rows

**Level:** Beginner–intermediate · **Suggested labels:** `help wanted`, `enhancement`

## What to build

CSV Inspector reports counts but does not show data. Add an optional
`preview_rows: int = 0` parameter. When it is positive, include a `preview` field
containing up to that many data rows as lists of strings. Exclude the header.

## Where to work

- Function: `inspect_csv` in `src/mcp_tools_lab/tools/csv_tool.py`
- Tests: `tests/test_csv_tool.py`
- Documentation: `docs/tool-guide.md`

## Example

`inspect_csv("name,age\nAda,20\nBob,21", preview_rows=1)` should include
`"preview": [["Ada", "20"]]`. Row counts should still cover the whole input.

## Acceptance checklist

- [ ] With the default `0`, preserve the current response (no `preview` field).
- [ ] With a positive value, return at most the requested number of data rows.
- [ ] Empty or header-only input returns `preview: []` when a preview is requested.
- [ ] Fewer available rows simply produce a shorter preview.
- [ ] Negative values raise a clear `ValueError`.
- [ ] Preserve quoted cells and uneven rows as parsed; do not pad or truncate cells.
- [ ] Malformed CSV still returns its existing validation error.
- [ ] Add tests and document the parameter.

**Hint:** The function already builds a list of data rows. List slicing is useful here.

Run `python -m pytest tests/test_csv_tool.py -q`, then `python -m pytest -q`.
