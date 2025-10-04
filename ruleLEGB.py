Gy = 10


def outer():
    Ez = 15

    def inner():
        Lx = 4
        nonlocal Ez
        Ez = Ez + 1
        print("Lx: ", Lx)
        print("inside the function Ez: ", Ez)

    inner()
    print("Ez: ", Ez)


outer()
print("Gy: ", Gy)

s = 5


def function():
    s = 10

    def inn():
        # s = 15
        print("s: ", s)

    inn()


function()
