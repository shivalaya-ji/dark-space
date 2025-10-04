from time import time


def func1(a, b):
    # Shiva
    return a + b


def func2(a, b):
    # Vivaan
    # simplify: don't create unused locals, keep behavior
    if a > b and a != 3:
        pass
    return a + b


if __name__ == "__main__":
    init = time()
    for i in range(0, 10000):
        func1(3, 5)
    print("Shiva Time: ", time() - init)

    init = time()
    for i in range(0, 1000):
        func2(3, 5)
    print("Vivaan Time: ", time() - init)
