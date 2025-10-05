import math

while True:
    user_input = input("Enter a non-negative number (integer or decimal, or type 'exit' to quit): ")
    if user_input.lower() in ["exit", "quit", "q"]:
        print("Goodbye!")
        break
    try:
        num = float(user_input)
        if num < 0:
            print("Error: Factorial is not defined for negative values.")
            continue
        result = math.gamma(num + 1)
        print(f"Factorial of {num} is approximately {result}")
    except ValueError:
        print("Error: Invalid input. Please enter a non-negative number or 'exit' to quit.")
    except OverflowError:
        print("Error: Number too large for calculation.")
