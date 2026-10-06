# Support semicolon and tab CSV delimiters

**Level:** Beginner–intermediate · **Suggested labels:** `help wanted`, `enhancement`

## What to build

Add an optional `delimiter: str = ","` argument to CSV Inspector. Support exactly
comma, semicolon, and tab. Users select the delimiter explicitly; no auto-detection is needed.

## Where to work

- Function: `inspect_csv` in `src/mcp_tools_lab/tools/csv_tool.py`
- Tests: `tests/test_csv_tool.py`
- Documentation: `docs/tool-guide.md`

## Example

`inspect_csv("name;age\nAda;20", delimiter=";")` should report two columns and one data row.
Use `delimiter="\t"` for tab-separated input.

## Acceptance checklist

- [ ] Calls without the new argument retain their current behavior.
- [ ] Support comma, semicolon, and the actual tab character.
- [ ] Reject empty, multi-character, and unsupported delimiters with a readable `ValueError`.
- [ ] Validate the delimiter even when input is empty.
- [ ] Pass the delimiter to `csv.reader`; keep its existing quoting behavior.
- [ ] Test a quoted cell containing the chosen delimiter, missing cells, and uneven rows.
- [ ] Document both new delimiter examples and add tests for invalid options.

**Hint:** `csv.reader` already accepts a `delimiter` keyword argument.
Coordinate with anyone implementing CSV previews or empty-header warnings; preserve
their changes if those land first. No preview functionality is required for this task.

Run `python -m pytest tests/test_csv_tool.py -q`, then `python -m pytest -q`.
