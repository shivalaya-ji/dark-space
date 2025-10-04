from fibonacci_sequence import fib_iter


def test_fib_iter_zero():
    assert fib_iter(0) == []


def test_fib_iter_small():
    assert fib_iter(1) == [0]
    assert fib_iter(2) == [0, 1]
    assert fib_iter(6) == [0, 1, 1, 2, 3, 5]
