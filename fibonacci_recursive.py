"""Recursive Fibonacci example."""


def recur_fibo(n: int) -> int:
    if n <= 1:
        return n
    return recur_fibo(n - 1) + recur_fibo(n - 2)


if __name__ == "__main__":
    nterms = int(input("How many terms? "))
    if nterms <= 0:
        print("Please enter a positive integer")
    else:
        print("Fibonacci sequence:")
        for i in range(nterms):
            print(recur_fibo(i))
