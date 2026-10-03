# Tool guide

All functions accept supplied strings and return dictionaries. They work without
MCP imports. Examples below show Python arguments; MCP uses the same parameter names.

## analyze_text(text)

`analyze_text("Hi hi!")` returns `characters=6`, `words=2`, `lines=1`,
`sentences=1`, and `frequent_words=[{"word": "hi", "count": 2}]`.
Characters include whitespace. Words are Unicode letter/digit sequences with
optional internal apostrophes; underscores separate words. Frequency is case-insensitive,
with ties ordered by first appearance. Lines follow `str.splitlines()`:
empty input has zero lines and a final newline does not add an extra line.
Sentence counting is a simple split on `.`, `!`, and `?`, not language-aware analysis.

## process_json(text, action="format", sort_keys=False)

Actions are `validate`, `format`, and `minify`. Formatting uses two spaces.
`process_json('{"a": 1}', action="minify")` returns
`{"valid": True, "output": '{"a":1}'}`. Validation returns only `valid` on success.
Malformed input returns `{"valid": False, "error": "..."}`.
JSON scalars such as `null` are supported. Duplicate object keys follow Python's
JSON behavior: the last value wins. Numbers use Python integers and floats;
float precision is not preserved exactly and overflowing floats are rejected.
NaN and Infinity are rejected. An unknown action raises `ValueError`.

## inspect_csv(text)

The first record contains column names; data-row counts exclude it. Input uses
commas and standard double-quote escaping. Results include `valid`, `columns`,
`row_count`, `missing_values`, and `inconsistent_rows`. Missing counts include
whitespace-only cells and absent trailing cells. Each missing-value entry has a
zero-based column `index`, so duplicate names remain distinguishable.
Inconsistent entries have `record`, `expected`, and `actual` field counts.
Record numbering begins at 1 for the header; it counts parsed CSV records, not
physical lines inside quoted values. Entirely blank lines are skipped by the parser.
Empty input returns empty lists and zero rows. Malformed quoting returns `valid=False`
and an error message. Extra cells are flagged but not counted as named columns.

## hash_text(text, algorithm="sha256")

Algorithms: `sha256`, `sha512`, `blake2b`. Returns `algorithm` and lowercase
hexadecimal `digest`. Text is encoded as UTF-8. Empty strings are supported.
These hashes compare content; this tool does not provide password storage.
Unknown algorithms raise `ValueError`.

## compare_text(before, after)

Returns `added_lines`, `removed_lines`, and a unified `diff` string. A replacement
counts as both removed and added lines. Identical inputs return an empty diff.
Comparison ignores CRLF versus LF and the presence of a final newline;
other whitespace is significant. Empty input is supported.

## convert_timestamp(value, direction="to_iso", unit="seconds")

`value` is a string. `to_iso` accepts Unix **seconds**, including fractions and
negative values. `to_unix` accepts an ISO 8601 date/time with `Z` or a UTC offset.
Both return `unix_seconds` and `iso_utc`. For example,
`convert_timestamp("1970-01-01T05:30:00+05:30", "to_unix")` returns zero seconds.
Set `unit="milliseconds"` to read a Unix value in milliseconds or include
`unix_milliseconds` when converting an ISO date. For example,
`convert_timestamp("1000", unit="milliseconds")` returns one Unix second, and
`convert_timestamp("1970-01-01T00:00:01Z", "to_unix", unit="milliseconds")`
returns 1000 Unix milliseconds. The default remains seconds; the converter does not
guess a unit from the size of a number.
Timezone-less dates are rejected so results do not depend on the machine's timezone.
Python datetime's year range (1–9999) and microsecond precision apply; finer fractional
seconds may be rounded. Invalid, infinite, or out-of-range values raise `ValueError`.

## inspect_url(url)

Accepts an absolute URL with a scheme and hostname. Returns `scheme`, `hostname`,
`port` (or `None`), `path`, `query_parameters`, and `fragment`. Query values are
decoded into lists, preserving duplicates and empty values. Paths remain encoded.
Missing schemes, bad ports, malformed IPv6, raw whitespace, and control characters
raise `ValueError`. This is a parser, not a security validator or reachability checker.
It makes no network requests and does not expose username/password fields in its result.

## Errors through MCP

JSON and CSV return structured validation errors for invalid content. Invalid tool
options, URLs, and timestamps raise `ValueError`; the MCP SDK turns these into tool
error results. The server remains available for subsequent requests.
