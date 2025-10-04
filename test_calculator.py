import math
import pytest

from Addition import parse_numbers, compute


def test_parse_numbers():
    assert parse_numbers("1 2 3") == [1.0, 2.0, 3.0]
    assert parse_numbers("4,5,6") == [4.0, 5.0, 6.0]
    with pytest.raises(ValueError):
        parse_numbers("")


def test_compute_add_sub_mul_div():
    assert compute("add", [1, 2, 3]) == 6
    assert compute("sub", [10, 1, 2]) == 7
    assert compute("mul", [2, 3, 4]) == 24
    assert compute("div", [100, 2, 5]) == 10


def test_compute_pow_mod_sqrt():
    assert pytest.approx(compute("pow", [2, 3]), rel=1e-12) == math.pow(2, 3)
    assert compute("mod", [10, 3]) == 10 % 3
    assert compute("sqrt", [9]) == 3
    with pytest.raises(ValueError):
        compute("sqrt", [1, 2])


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        compute("div", [1, 0])
