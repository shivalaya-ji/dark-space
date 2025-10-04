"""Interactive calculator: add, subtract, multiply, divide, history, quit.

Features:
- Menu-driven: choose operation or view history or quit.
- Accept multiple numbers (space- or comma-separated) for operations.
- Keeps a short history of calculations in this session.
"""

from typing import List
from pathlib import Path
import math


def parse_numbers(s: str) -> List[float]:
	"""Parse a string of numbers separated by spaces or commas into floats."""
	parts = [p.strip() for p in s.replace(",", " ").split() if p.strip()]
	if not parts:
		raise ValueError("no numbers provided")
	nums = []
	for p in parts:
		try:
			nums.append(float(p))
		except ValueError:
			raise ValueError(f"invalid number: {p!r}")
	return nums


def compute(op: str, nums: List[float]) -> float:
	"""Compute the result for operation op on the list of numbers.

	op in {'add','sub','mul','div'}
	"""
	if op == "add":
		return sum(nums)
	if op == "sub":
		# subtract all following numbers from the first
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
				raise ZeroDivisionError("division by zero")
			total /= x
		return total
	if op == "pow":
		# power: x ** y ** z (left-associative here for simplicity)
		it = iter(nums)
		total = next(it)
		for x in it:
			total = math.pow(total, x)
		return total
	if op == "mod":
		it = iter(nums)
		total = next(it)
		for x in it:
			total = total % x
		return total
	if op == "sqrt":
		# sqrt: only first number used
		if len(nums) != 1:
			raise ValueError("sqrt requires exactly one argument")
		if nums[0] < 0:
			raise ValueError("sqrt of negative number")
		return math.sqrt(nums[0])
	raise ValueError(f"unknown operation: {op}")


def print_menu() -> None:
	print("\nSimple calculator — choose an operation:")
	print("  add  - add numbers")
	print("  sub  - subtract (first minus others)")
	print("  mul  - multiply numbers")
	print("  div  - divide (first divided by next etc.)")
	print("  history - show session history")
	print("  q/quit/exit - quit")


def main() -> None:
	print("Namaste! Simple interactive calculator.")
	hist_file = Path.home() / ".calculator_history"
	history: List[str] = []
	# load existing history
	try:
		if hist_file.exists():
			with hist_file.open("r", encoding="utf8") as f:
				history = [line.rstrip("\n") for line in f if line.strip()]
	except Exception:
		# ignore any errors reading history
		history = []
	while True:
		print_menu()
		choice = input("Operation> ").strip().lower()
		if choice in {"q", "quit", "exit"}:
			print("Goodbye!")
			break
		if choice == "history":
			if not history:
				print("(no history yet)")
			else:
				print("History:")
				for i, h in enumerate(history, 1):
					print(f" {i}. {h}")
			continue
		if choice not in {"add", "sub", "mul", "div"}:
			print("Unknown command. Please choose add, sub, mul, div, history, or q.")
			continue

		nums_input = input("Enter numbers (space or comma separated): ").strip()
		try:
			nums = parse_numbers(nums_input)
		except ValueError as e:
			print(e)
			continue

		try:
			result = compute(choice, nums)
		except ZeroDivisionError as e:
			print(e)
			continue
		except Exception as e:
			print(f"Error: {e}")
			continue

		expr = f"{choice}({', '.join(map(str, nums))}) = {result}"
		print(expr)
		history.append(expr)
		# append to history file
		try:
			with hist_file.open("a", encoding="utf8") as f:
				f.write(expr + "\n")
		except Exception:
			pass


if __name__ == "__main__":
	main()
