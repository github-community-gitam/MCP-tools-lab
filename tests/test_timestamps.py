import pytest
from mcp_tools_lab.tools.timestamps import convert_timestamp


def test_epoch_and_offset():
    assert convert_timestamp("0")["iso_utc"] == "1970-01-01T00:00:00Z"
    assert convert_timestamp("1970-01-01T05:30:00+05:30", "to_unix")["unix_seconds"] == 0


def test_fractional_and_negative_seconds():
    assert convert_timestamp("-0.5")["iso_utc"] == "1969-12-31T23:59:59.500000Z"
    assert convert_timestamp("1970-01-01T00:00:00.500000Z", "to_unix")["unix_seconds"] == 0.5


@pytest.mark.parametrize(
    "value,seconds",
    [("1000", 1), ("0", 0), ("-500", -0.5), ("500.5", 0.5005)],
)
def test_millisecond_input(value, seconds):
    result = convert_timestamp(value, unit="milliseconds")
    assert result["unix_seconds"] == seconds
    assert result["unix_milliseconds"] == float(value)


def test_millisecond_output_from_iso_offset():
    result = convert_timestamp("1970-01-01T05:30:01+05:30", "to_unix", unit="milliseconds")
    assert result == {
        "unix_seconds": 1,
        "unix_milliseconds": 1000,
        "iso_utc": "1970-01-01T00:00:01Z",
    }


def test_default_result_shape_is_unchanged():
    assert convert_timestamp("1") == {
        "unix_seconds": 1,
        "iso_utc": "1970-01-01T00:00:01Z",
    }


def test_invalid_unit():
    with pytest.raises(ValueError, match="unit must be seconds or milliseconds"):
        convert_timestamp("1", unit="minutes")


@pytest.mark.parametrize("value,direction", [("nan", "to_iso"), ("inf", "to_iso"),
    ("1e99", "to_iso"), ("oops", "to_iso"), ("2026-01-01", "to_unix"),
    ("2026-01-01T12:00:00", "to_unix"), ("0", "wrong")])
def test_invalid_input(value, direction):
    with pytest.raises(ValueError, match="Cannot convert"):
        convert_timestamp(value, direction)
