for row in range(6):
    for col in range(7):
        if any(
            (
                (row == 0 and col % 3 != 0),
                (row == 1 and col % 3 == 0),
                (row - col == 2),
                (row + col == 8),
            )
        ):
            print("*", end=" ")
        else:
            print(end=" ")
    print()
