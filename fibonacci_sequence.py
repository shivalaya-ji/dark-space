"""Iterative Fibonacci utilities."""

from typing import List


def fib_iter(nterms: int) -> List[int]:
    """Return a list with the first nterms of the Fibonacci sequence."""
    if nterms <= 0:
        return []
    seq = []
    n1, n2 = 0, 1
    count = 0
    while count < nterms:
        seq.append(n1)
        n1, n2 = n2, n1 + n2
        count += 1
    return seq


if __name__ == "__main__":
    nterms = int(input("How many terms? "))
    seq = fib_iter(nterms)
    if not seq:
        print("Please enter a positive integer")
    else:
        print("Fibonacci sequence:")
        for v in seq:
            print(v)
