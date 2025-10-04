"""Factorial helpers (snake_case module) for tests and CLI."""

import math
from typing import Union


def parse_number(s: str) -> float:
    """Parse a user-entered number string into a float.

    Accepts strings like '1,000', '1_000', '5.0', '4.5', with optional
    whitespace. Raises ValueError on invalid input.
    """
    if not isinstance(s, str):
        raise ValueError("input must be a string")
    s_clean = s.strip()
    if s_clean == "":
        raise ValueError("empty input")
    s_clean = s_clean.replace(",", "").replace("_", "").replace(" ", "")
    try:
        return float(s_clean)
    except ValueError:
        raise ValueError(f"Invalid numeric input: {s!r}")


def compute_factorial_from_float(x: float) -> Union[int, float]:
    """Compute factorial for numeric x.

    - Integers >= 0 -> exact factorial (int)
    - Non-integers -> math.gamma(x+1) (float)
    """
    if not isinstance(x, (int, float)):
        raise ValueError("x must be a numeric type")
    if float(x).is_integer():
        n = int(x)
        if n < 0:
            raise ValueError("factorial not defined for negative integers")
        return math.factorial(n)
    y = x + 1
    if abs(y - round(y)) < 1e-12 and round(y) <= 0:
        raise ValueError("factorial not defined for this value (gamma pole)")
    return math.gamma(y)


if __name__ == "__main__":
    s = input("Enter a number: ")
    try:
        x = parse_number(s)
        r = compute_factorial_from_float(x)
    except ValueError as e:
        print(e)
    else:
        if float(x).is_integer():
            print(f"The factorial of {int(x)} is {r}")
        else:
            print(f"The factorial (via Gamma) of {x} is approximately {r:.6g}")
"""Factorial helpers (snake_case module) for tests and CLI.

Provides:
- parse_number(s: str) -> float
- compute_factorial_from_float(x: float) -> int | float
"""

import math
from typing import Union


def parse_number(s: str) -> float:
    if not isinstance(s, str):
        raise ValueError("input must be a string")
    s_clean = s.strip()
    if s_clean == "":
        raise ValueError("empty input")
    s_clean = s_clean.replace(",", "").replace("_", "").replace(" ", "")
    try:
        return float(s_clean)
    except ValueError:
        raise ValueError(f"Invalid numeric input: {s!r}")


def compute_factorial_from_float(x: float) -> Union[int, float]:
    if not isinstance(x, (int, float)):
        raise ValueError("x must be a numeric type")
    if float(x).is_integer():
        n = int(x)
        if n < 0:
            raise ValueError("factorial not defined for negative integers")
        return math.factorial(n)
    y = x + 1
    if abs(y - round(y)) < 1e-12 and round(y) <= 0:
        raise ValueError("factorial not defined for this value (gamma pole)")
    return math.gamma(y)


if __name__ == "__main__":
    s = input("Enter a number: ")
    try:
        x = parse_number(s)
        r = compute_factorial_from_float(x)
    except ValueError as e:
        print(e)
    else:
        if float(x).is_integer():
            print(f"The factorial of {int(x)} is {r}")
        else:
            print(f"The factorial (via Gamma) of {x} is approximately {r:.6g}")
"""Factorial helpers (single clean implementation).

Provides parse_number and compute_factorial_from_float used by tests.
"""

import math
from typing import Union


def parse_number(s: str) -> float:
    """Parse a user-entered number string into a float.

    Accepts strings like '1,000', '1_000', '5.0', '4.5', with optional
    whitespace. Raises ValueError on invalid input.
    """
    if not isinstance(s, str):
        raise ValueError("input must be a string")
    s_clean = s.strip()
    if s_clean == "":
        raise ValueError("empty input")
    s_clean = s_clean.replace(",", "").replace("_", "").replace(" ", "")
    try:
        return float(s_clean)
    except ValueError:
        raise ValueError(f"Invalid numeric input: {s!r}")


def compute_factorial_from_float(x: float) -> Union[int, float]:
    """Compute factorial for numeric x.

    - Integers >= 0 -> exact factorial (int)
    - Non-integers -> math.gamma(x+1) (float)
    """
    if not isinstance(x, (int, float)):
        raise ValueError("x must be a numeric type")
    if float(x).is_integer():
        n = int(x)
        if n < 0:
            raise ValueError("factorial not defined for negative integers")
        return math.factorial(n)
    y = x + 1
    if abs(y - round(y)) < 1e-12 and round(y) <= 0:
        raise ValueError("factorial not defined for this value (gamma pole)")
    return math.gamma(y)


def main() -> None:
    s = input("Enter a number: ")
    try:
        x = parse_number(s)
        r = compute_factorial_from_float(x)
    except ValueError as e:
        print(e)
        return
    if float(x).is_integer():
        print(f"The factorial of {int(x)} is {r}")
    else:
        print(f"The factorial (via Gamma) of {x} is approximately {r:.6g}")


if __name__ == "__main__":
    main()
"""Factorial utility: parse flexible numeric input and compute factorial.

This module exposes small helper functions that are testable:
- parse_number(s) -> float
- compute_factorial_from_float(x) -> int|float

The script still has a friendly CLI via `main()`.
"""

import math
from typing import Union


def parse_number(s: str) -> float:
    """Parse a user-entered number string into a float.

    Accepts inputs like:
    - '1,000' or '1_000' (commas/underscores ignored)
    - leading/trailing whitespace
    - standard float and scientific notation ('1e3')

    Raises ValueError on invalid input.
    """
    if not isinstance(s, str):
        raise ValueError("input must be a string")
    s_clean = s.strip()
    if s_clean == "":
        raise ValueError("empty input")
    # Allow common thousands separators and underscores
    s_clean = s_clean.replace(",", "")
    s_clean = s_clean.replace("_", "")
    # Remove internal spaces that users occasionally include
    s_clean = s_clean.replace(" ", "")
    # Now convert
    try:
        return float(s_clean)
    except ValueError:
        raise ValueError(f"Invalid numeric input: {s!r}")


def compute_factorial_from_float(x: float) -> Union[int, float]:
    """Compute factorial for the given numeric value x.

    - If x is an integer >= 0 -> return exact integer factorial.
    - If x is a non-integer -> return math.gamma(x+1) (float).

    Raises ValueError for negative integers or gamma poles.
    """
    if not isinstance(x, (int, float)):
        raise ValueError("x must be a numeric type")

    # Treat values like 5.0 as integers
    if float(x).is_integer():
        n = int(x)
        if n < 0:
            raise ValueError("factorial not defined for negative integers")
        return math.factorial(n)
    else:
        y = x + 1
        # Detect poles where y is a non-positive integer.
        # Gamma has poles at 0, -1, -2, ... so we must reject those values.
        if abs(y - round(y)) < 1e-12 and round(y) <= 0:
            raise ValueError(
                "factorial not defined for this value (pole in Gamma function)"
            )
        return math.gamma(y)


def main() -> None:
    s = input("Enter a number: ")
    try:
        x = parse_number(s)
    except ValueError as e:
        print(e)
        return

    try:
        result = compute_factorial_from_float(x)
    except ValueError as e:
        print(e)
        return

    if float(x).is_integer():
        print(f"The factorial of {int(x)} is {result}")
    else:
        # Wrap long formatted output to satisfy line-length checks
        approx = f"{result:.6g}"
        print(
            f"The factorial (via Gamma) of {x} is approximately {approx}"
        )


if __name__ == "__main__":
    main()
"""Factorial utility: parse flexible numeric input and compute factorial.

This module exposes small helper functions that are testable:
- parse_number(s) -> float
- compute_factorial_from_float(x) -> int|float

The script still has a friendly CLI via `main()`.
"""

import math
from typing import Union


def parse_number(s: str) -> float:
    """Parse a user-entered number string into a float.

    Accepts inputs like:
    - '1,000' or '1_000' (commas/underscores ignored)
    - leading/trailing whitespace
    - standard float and scientific notation ('1e3')

    Raises ValueError on invalid input.
    """
    if not isinstance(s, str):
        raise ValueError("input must be a string")
    s_clean = s.strip()
    if s_clean == "":
        raise ValueError("empty input")
    # Allow common thousands separators and underscores
    s_clean = s_clean.replace(",", "")
    s_clean = s_clean.replace("_", "")
    # Remove internal spaces that users occasionally include
    s_clean = s_clean.replace(" ", "")
    # Now convert
    try:
        return float(s_clean)
    except ValueError:
        raise ValueError(f"Invalid numeric input: {s!r}")


def compute_factorial_from_float(x: float) -> Union[int, float]:
    """Compute factorial for the given numeric value x.

    - If x is an integer >= 0 -> return exact integer factorial.
    - If x is a non-integer -> return math.gamma(x+1) (float).

    Raises ValueError for negative integers or gamma poles.
    """
    if not isinstance(x, (int, float)):
        raise ValueError("x must be a numeric type")

    # Treat values like 5.0 as integers
    if float(x).is_integer():
        n = int(x)
        if n < 0:
            raise ValueError("factorial not defined for negative integers")
        return math.factorial(n)
    else:
        y = x + 1
        # Detect poles where y is a non-positive integer.
        # Gamma has poles at 0, -1, -2, ... so we must reject those values.
        if abs(y - round(y)) < 1e-12 and round(y) <= 0:
            raise ValueError(
                "factorial not defined for this value (pole in Gamma function)"
            )
        return math.gamma(y)


def main() -> None:
    s = input("Enter a number: ")
    try:
        x = parse_number(s)
    except ValueError as e:
        print(e)
        return

    try:
        result = compute_factorial_from_float(x)
    except ValueError as e:
        print(e)
        return

    if float(x).is_integer():
        print(f"The factorial of {int(x)} is {result}")
    else:
        # Wrap long formatted output to satisfy line-length checks
        approx = f"{result:.6g}"
        print(f"The factorial (via Gamma) of {x} is approximately {approx}")


if __name__ == "__main__":
    main()
