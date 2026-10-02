"""
Exercise 2: Conditionals
========================
Topics covered:
  - if / elif / else chains
  - Comparison and logical operators (and, or, not)
  - Ternary (inline) expressions
  - Nested conditions
  - Guard clauses (early return)
"""


def grade_score(score: float) -> str:
    """
    Convert a numeric score (0–100) into a letter grade.

    Grading scale:
        90–100  ->  A
        80–89   ->  B
        70–79   ->  C
        60–69   ->  D
        0–59    ->  F

    Args:
        score: A numeric value between 0 and 100 (inclusive).

    Returns:
        A single letter grade ('A'–'F').

    Raises:
        ValueError: if score is outside [0, 100].
    """
    # Guard clause – reject invalid input immediately
    if not (0 <= score <= 100):
        raise ValueError(f"Score must be between 0 and 100; got {score}.")

    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


def categorise_bmi(weight_kg: float, height_m: float) -> str:
    """
    Calculate BMI and return the WHO category.

    Categories:
        BMI < 18.5          ->  Underweight
        18.5 ≤ BMI < 25.0   ->  Normal weight
        25.0 ≤ BMI < 30.0   ->  Overweight
        BMI ≥ 30.0          ->  Obese

    Args:
        weight_kg: Body weight in kilograms (must be > 0).
        height_m:  Height in metres (must be > 0).

    Returns:
        A string describing the BMI category.

    Raises:
        ValueError: if weight or height are not positive.
    """
    if weight_kg <= 0 or height_m <= 0:
        raise ValueError("Weight and height must be positive numbers.")

    bmi = weight_kg / (height_m ** 2)

    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 25.0:
        category = "Normal weight"
    elif bmi < 30.0:
        category = "Overweight"
    else:
        category = "Obese"

    return f"BMI = {bmi:.1f}  ->  {category}"


def fizzbuzz(n: int) -> str:
    """
    Classic FizzBuzz for a single number.

    Rules:
        Divisible by both 3 and 5  ->  'FizzBuzz'
        Divisible by 3 only        ->  'Fizz'
        Divisible by 5 only        ->  'Buzz'
        Otherwise                  ->  the number as a string

    Args:
        n: Any integer.

    Returns:
        The appropriate FizzBuzz string.
    """
    # Check the combined case first (order matters!)
    if n % 15 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return str(n)


def ticket_price(age: int, is_member: bool) -> float:
    """
    Determine cinema ticket price based on age and membership.

    Pricing rules:
        Members always pay £5.00.
        Under 5   ->  free (£0.00)
        5–17      ->  £7.50  (child)
        18–64     ->  £12.00 (adult)
        65+       ->  £8.00  (senior)

    Args:
        age:       Age in whole years (must be ≥ 0).
        is_member: Whether the person holds a membership card.

    Returns:
        Price as a float.

    Raises:
        ValueError: if age is negative.
    """
    if age < 0:
        raise ValueError("Age cannot be negative.")

    if is_member:
        return 5.00

    if age < 5:
        return 0.00
    elif age < 18:
        return 7.50
    elif age < 65:
        return 12.00
    else:
        return 8.00


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    print("=" * 45)
    print("  Exercise 2 – Conditionals")
    print("=" * 45)
    print()

    # --- Grade calculator ---
    print("--- Grade Calculator ---")
    for score in [95, 83, 74, 61, 45]:
        print(f"  Score {score:>3}  ->  Grade {grade_score(score)}")
    print()

    # --- BMI ---
    print("--- BMI Categoriser ---")
    examples = [(50, 1.70), (70, 1.75), (90, 1.75), (110, 1.70)]
    for w, h in examples:
        print(f"  Weight={w}kg, Height={h}m  ->  {categorise_bmi(w, h)}")
    print()

    # --- FizzBuzz 1-20 ---
    print("--- FizzBuzz (1–20) ---")
    results = [fizzbuzz(i) for i in range(1, 21)]
    print("  " + ", ".join(results))
    print()

    # --- Ticket pricing ---
    print("--- Ticket Pricing ---")
    test_cases = [(3, False), (10, False), (10, True), (30, False), (70, False)]
    for age, member in test_cases:
        price = ticket_price(age, member)
        tag = "(member)" if member else ""
        print(f"  Age={age:<3} {tag:<8}  ->  £{price:.2f}")
