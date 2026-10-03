# Choose JSON indentation

**Level:** Beginner · **Suggested labels:** `good first issue`, `enhancement`

## What to build

Pretty JSON currently always uses two spaces. Add an optional `indent` parameter
that accepts `2` or `4` and defaults to `2`.

## Where to work

- Function: `process_json` in `src/mcp_tools_lab/tools/json_tool.py`
- Tests: `tests/test_json_tool.py`
- Documentation: `docs/tool-guide.md`

## Example

`process_json('{"a":1}', indent=4)` should produce an `output` string with four
spaces before `"a"`. Calls without `indent` should produce the existing output.

## Acceptance checklist

- [ ] Add a typed `indent` parameter with default `2`.
- [ ] Formatting supports both allowed values, including nested objects.
- [ ] Unsupported values raise a readable `ValueError`.
- [ ] Validate the option for every action, but keep valid `minify` and `validate` results unchanged.
- [ ] Add tests for the default, four spaces, nested JSON, and unsupported values.
- [ ] Update the tool docstring and guide.

**Hint:** Python's `json.dumps` already has an `indent` argument. The server reads
the function signature automatically; you do not need to edit `server.py`.

Run `python -m pytest tests/test_json_tool.py -q`, then `python -m pytest -q`.
