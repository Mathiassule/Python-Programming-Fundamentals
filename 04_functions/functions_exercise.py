"""
Exercise 4: Functions
=====================
Topics covered:
  - Defining functions with type hints
  - Default parameter values
  - *args and **kwargs
  - Docstrings
  - Recursion
  - Higher-order functions (passing functions as arguments)
  - Lambda expressions
"""

from typing import Callable


# ---------------------------------------------------------------------------
# 4-A  Default parameters
# ---------------------------------------------------------------------------
def greet(name: str, greeting: str = "Hello", punctuation: str = "!") -> str:
    """
    Return a customisable greeting string.

    Args:
        name:        Person to greet.
        greeting:    Word to use (default 'Hello').
        punctuation: Character appended at the end (default '!').

    Returns:
        Formatted greeting string.
    """
    return f"{greeting}, {name}{punctuation}"


# ---------------------------------------------------------------------------
# 4-B  *args – variable positional arguments
# ---------------------------------------------------------------------------
def total_cost(*prices: float, tax_rate: float = 0.20) -> float:
    """
    Calculate the total cost of items including tax.

    Args:
        *prices:   Individual item prices (any number of floats).
        tax_rate:  VAT / sales-tax rate as a decimal (default 20 %).

    Returns:
        Total cost rounded to 2 decimal places.
    """
    subtotal = sum(prices)
    return round(subtotal * (1 + tax_rate), 2)


# ---------------------------------------------------------------------------
# 4-C  **kwargs – keyword arguments forwarded to formatting
# ---------------------------------------------------------------------------
def build_profile(**kwargs: str) -> str:
    """
    Build a multi-line profile string from arbitrary keyword arguments.

    Args:
        **kwargs: Any key=value pairs describing a person.

    Returns:
        A formatted string with each key–value on its own line.
    """
    lines = [f"  {key.replace('_', ' ').title():<20}: {value}"
             for key, value in kwargs.items()]
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# 4-D  Recursion
# ---------------------------------------------------------------------------
def fibonacci(n: int) -> int:
    """
    Return the n-th Fibonacci number using recursion.

    F(0) = 0,  F(1) = 1,  F(n) = F(n-1) + F(n-2)

    Args:
        n: Index in the Fibonacci sequence (must be ≥ 0).

    Returns:
        The n-th Fibonacci number.

    Raises:
        ValueError: if n is negative.
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer.")
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def factorial(n: int) -> int:
    """
    Return n! using recursion.

    Args:
        n: A non-negative integer.

    Returns:
        n factorial.

    Raises:
        ValueError: if n is negative.
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer.")
    if n == 0:
        return 1
    return n * factorial(n - 1)


# ---------------------------------------------------------------------------
# 4-E  Higher-order functions
# ---------------------------------------------------------------------------
def apply_twice(func: Callable[[float], float], value: float) -> float:
    """
    Apply a single-argument function to a value twice.

    Args:
        func:  A callable that accepts and returns a float.
        value: The initial value.

    Returns:
        func(func(value))
    """
    return func(func(value))


def make_multiplier(factor: float) -> Callable[[float], float]:
    """
    Return a function that multiplies its argument by `factor`.

    This demonstrates closures and factory functions.

    Args:
        factor: The multiplier.

    Returns:
        A function float → float.
    """
    def multiplier(x: float) -> float:
        return x * factor
    return multiplier


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    print("=" * 45)
    print("  Exercise 4 – Functions")
    print("=" * 45)
    print()

    # Greet
    print(greet("World"))
    print(greet("Alice", greeting="Good morning", punctuation="."))
    print()

    # Total cost
    items = [9.99, 4.50, 12.00]
    print(f"Items: {items}")
    print(f"Total (20% tax): £{total_cost(*items)}")
    print(f"Total (5% tax) : £{total_cost(*items, tax_rate=0.05)}")
    print()

    # Build profile
    print("User profile:")
    print(build_profile(first_name="Grace", last_name="Hopper",
                        occupation="Mathematician", birth_year="1906"))
    print()

    # Fibonacci
    print("Fibonacci sequence F(0)–F(10):")
    print(" ", [fibonacci(i) for i in range(11)])
    print()

    # Factorial
    for k in [0, 1, 5, 10]:
        print(f"  {k}! = {factorial(k)}")
    print()

    # Higher-order
    double = make_multiplier(2)
    print(f"apply_twice(double, 3) → {apply_twice(double, 3)}")
    print(f"apply_twice(lambda x: x+1, 10) → {apply_twice(lambda x: x + 1, 10)}")
