"""
Exercise 1: Variables and Data Types
=====================================
Topics covered:
  - Declaring variables of different types
  - Type conversion (casting)
  - f-strings for formatted output
  - Basic arithmetic with type awareness
"""


def describe_person(name: str, age: int, height_cm: float, is_student: bool) -> str:
    """
    Build a human-readable description of a person from basic data.

    Args:
        name:       Full name of the person.
        age:        Age in whole years.
        height_cm:  Height in centimetres (can include decimals).
        is_student: Whether the person is currently a student.

    Returns:
        A formatted string describing the person.
    """
    status = "a student" if is_student else "not a student"
    height_m = height_cm / 100  # convert centimetres → metres

    return (
        f"Name   : {name}\n"
        f"Age    : {age} years old\n"
        f"Height : {height_m:.2f} m ({height_cm} cm)\n"
        f"Status : {name.split()[0]} is {status}."
    )


def type_conversion_demo() -> None:
    """
    Demonstrate common type conversions and show that Python is
    strongly (but dynamically) typed.
    """
    # --- integer ↔ float ---
    whole_number: int = 7
    as_float: float = float(whole_number)      # 7.0
    back_to_int: int = int(as_float * 1.5)    # 10  (truncates, does not round)

    # --- string ↔ number ---
    price_str: str = "19.99"
    price_float: float = float(price_str)
    price_int: int = int(price_float)          # 19  (truncates decimal)

    # --- bool ↔ int (Python bools are ints!) ---
    flag: bool = True
    flag_as_int: int = int(flag)               # 1

    print("=== Type Conversion Demo ===")
    print(f"  int    {whole_number!r:>8}  →  float  {as_float!r}")
    print(f"  float  {as_float * 1.5!r:>8}  →  int    {back_to_int!r}  (truncated)")
    print(f"  str    {price_str!r:>8}  →  float  {price_float!r}")
    print(f"  float  {price_float!r:>8}  →  int    {price_int!r}  (truncated)")
    print(f"  bool   {flag!r:>8}  →  int    {flag_as_int!r}")
    print()


def collect_basic_stats(numbers: list) -> dict:
    """
    Compute simple statistics for a list of numbers.

    Args:
        numbers: A non-empty list of numeric values.

    Returns:
        A dict with keys: count, total, mean, minimum, maximum.

    Raises:
        ValueError: if the list is empty.
    """
    if not numbers:
        raise ValueError("Cannot compute stats for an empty list.")

    return {
        "count":   len(numbers),
        "total":   sum(numbers),
        "mean":    sum(numbers) / len(numbers),
        "minimum": min(numbers),
        "maximum": max(numbers),
    }


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    print("=" * 45)
    print("  Exercise 1 – Variables and Data Types")
    print("=" * 45)
    print()

    # --- describe_person ---
    description = describe_person(
        name="Ada Lovelace",
        age=36,
        height_cm=165.5,
        is_student=False,
    )
    print(description)
    print()

    # --- type conversions ---
    type_conversion_demo()

    # --- basic stats ---
    sample_data = [4, 8, 15, 16, 23, 42]
    stats = collect_basic_stats(sample_data)
    print("=== Basic Statistics ===")
    print(f"  Data    : {sample_data}")
    for key, value in stats.items():
        print(f"  {key:<8}: {value}")
