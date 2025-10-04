import math
import pytest

from factorial import parse_number, compute_factorial_from_float


def test_parse_int_and_compute():
    x = parse_number("5")
    assert isinstance(x, float)
    assert compute_factorial_from_float(x) == 120


def test_parse_int_like_float():
    x = parse_number("5.0")
    assert compute_factorial_from_float(x) == 120


def test_non_integer_gamma():
    x = parse_number("4.5")
    expected = math.gamma(x + 1)
    got = compute_factorial_from_float(x)
    assert pytest.approx(got, rel=1e-12) == expected


def test_invalid_input_raises():
    with pytest.raises(ValueError):
        parse_number("abc")


def test_negative_integer_error():
    x = parse_number("-3")
    with pytest.raises(ValueError):
        compute_factorial_from_float(x)


def test_gamma_pole():
    # x = -1.0 -> x+1 = 0 -> pole
    x = parse_number("-1.0")
    with pytest.raises(ValueError):
        compute_factorial_from_float(x)
