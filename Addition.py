from typing import List
from pathlib import Path
import math

def parse_numbers(s: str) -> List[float]:
    """Parse a string of numbers separated by spaces or commas into floats."""
    parts = [p.strip() for p in s.replace(",", " ").split() if p.strip()]
    if not parts:
        raise ValueError("No numbers provided! Example: 2 3 4 or 1,2,3")
    nums = []
    for p in parts:
        try:
            nums.append(float(p))
        except ValueError:
            raise ValueError(f"Invalid number encountered: {p!r}")
    return nums

def compute(op: str, nums: List[float]) -> float:
    """Compute result for given operation and list of numbers."""
    if op == "add":
        return sum(nums)
    if op == "sub":
        it = iter(nums)
        total = next(it)
        for x in it:
            total -= x
        return total
    if op == "mul":
        total = 1.0
        for x in nums:
            total *= x
        return total
    if op == "div":
        it = iter(nums)
        total = next(it)
        for x in it:
            if x == 0:
                raise ZeroDivisionError("Division by zero is undefined.")
            total /= x
        return total
    if op == "pow":
        it = iter(nums)
        total = next(it)
        for x in it:
            try:
                total = math.pow(total, x)
            except (ValueError, OverflowError) as e:
                raise ValueError(f"Invalid power operation: {e}")
        return total
    if op == "mod":
        it = iter(nums)
        total = next(it)
        for x in it:
            if x == 0:
                raise ZeroDivisionError("Modulo by zero is undefined.")
            total = total % x
        return total
    if op == "sqrt":
        if len(nums) != 1:
            raise ValueError("Sqrt requires exactly one argument. Example: 9")
        if nums[0] < 0:
            raise ValueError("Sqrt of negative number is not defined for real numbers.")
        return math.sqrt(nums[0])
    raise ValueError(f"Unknown operation: {op}")

def print_menu() -> None:
    print("\nOperations Menu:")
    print("  add   - addition (2 3 4 → 2+3+4)")
    print("  sub   - subtraction (first minus rest)")
    print("  mul   - multiplication")
    print("  div   - division (first divided by next etc.)")
    print("  pow   - exponentiation (left-assoc.; 2 3 2 → (2**3)**2 )")
    print("  mod   - modulo (remainder)")
    print("  sqrt  - square root (of one positive number)")
    print("  history - show all calculations this session")
    print("  clear   - clear session history (doesn't delete file)")
    print("  q/quit/exit - quit")

def main() -> None:
    print("Namaste! Mature Interactive Calculator.\n")
    hist_file = Path.home() / ".calculator_history"
    history: List[str] = []
    # Load file history if exists
    try:
        if hist_file.exists():
            with hist_file.open("r", encoding="utf8") as f:
                file_hist = [line.rstrip("\n") for line in f if line.strip()]
                history.extend(file_hist)
    except Exception:
        pass  # Ignore file errors
    
    session_history: List[str] = []

    while True:
        print_menu()
        choice = input("Operation> ").strip().lower()
        if choice in {"q", "quit", "exit"}:
            print("Goodbye!")
            break
        if choice == "history":
            if not session_history:
                print("(No calculations yet in this session.)")
            else:
                print("Session history:")
                for i, h in enumerate(session_history, 1):
                    print(f" {i}. {h}")
            continue
        if choice == "clear":
            session_history.clear()
            print("Session history cleared.")
            continue
        if choice not in {"add", "sub", "mul", "div", "pow", "mod", "sqrt"}:
            print("Unknown command. Type 'add', 'mul', etc. or 'q' to quit. (Use 'history' to view past calculations.)")
            continue
        # Input numbers
        nums_input = input("Enter numbers (space/comma separated): ").strip()
        try:
            nums = parse_numbers(nums_input)
        except ValueError as e:
            print(f"Input Error: {e}")
            continue

        try:
            result = compute(choice, nums)
            # Neatly format result, rounded if float
            if isinstance(result, float):
                result_str = f"{result:.8g}"
            else:
                result_str = str(result)
            expr = f"{choice}({', '.join(map(str, nums))}) = {result_str}"
            print(expr)
            session_history.append(expr)
            # append to file history
            try:
                with hist_file.open("a", encoding="utf8") as f:
                    f.write(expr + "\n")
            except Exception:
                pass
        except ZeroDivisionError as e:
            print(f"Math Error: {e}")
        except ValueError as e:
            print(f"Math Error: {e}")
        except Exception as e:
            print(f"Unexpected Error: {e}")

if __name__ == "__main__":
    main()
