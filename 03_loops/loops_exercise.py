"""
Exercise 3: Loops
=================
Topics covered:
  - for loops with range()
  - while loops with sentinel values
  - break and continue
  - List comprehensions
  - Nested loops
  - enumerate() and zip()
"""


def sum_of_multiples(limit: int, *factors: int) -> int:
    """
    Return the sum of all unique integers below `limit` that are
    multiples of ANY of the given factors.

    Example:
        sum_of_multiples(10, 3, 5) → 23  (3+5+6+9 = 23)

    Args:
        limit:   Upper bound (exclusive).
        *factors: One or more divisors to test against.

    Returns:
        Integer sum.
    """
    return sum(
        n for n in range(limit)
        if any(n % f == 0 for f in factors)
    )


def countdown(start: int) -> list:
    """
    Build a countdown list from `start` down to 0 using a while loop.

    Args:
        start: A non-negative integer to count down from.

    Returns:
        A list [start, start-1, …, 1, 0, 'Blast off!'].

    Raises:
        ValueError: if start is negative.
    """
    if start < 0:
        raise ValueError("start must be a non-negative integer.")

    sequence = []
    current = start
    while current >= 0:
        sequence.append(current)
        current -= 1
    sequence.append("Blast off!")
    return sequence


def flatten(nested: list) -> list:
    """
    Flatten one level of nesting from a list of lists using a for loop.

    Args:
        nested: A list whose elements may themselves be lists.

    Returns:
        A new flat list.

    Example:
        flatten([[1, 2], [3, 4], [5]]) → [1, 2, 3, 4, 5]
    """
    flat = []
    for sublist in nested:
        for item in sublist:
            flat.append(item)
    return flat


def multiplication_table(size: int) -> list[list[int]]:
    """
    Generate an n×n multiplication table as a list of lists.

    Args:
        size: Dimension of the table (e.g. 5 → 5×5 table).

    Returns:
        A 2-D list where result[i][j] = (i+1) * (j+1).
    """
    return [
        [(row + 1) * (col + 1) for col in range(size)]
        for row in range(size)
    ]


def first_prime_above(n: int) -> int:
    """
    Find the first prime number strictly greater than n.

    Uses a while loop with a break to stop as soon as the prime is found.

    Args:
        n: A non-negative integer.

    Returns:
        The smallest prime > n.
    """
    def is_prime(num: int) -> bool:
        if num < 2:
            return False
        for divisor in range(2, int(num ** 0.5) + 1):
            if num % divisor == 0:
                return False
        return True

    candidate = n + 1
    while True:
        if is_prime(candidate):
            return candidate
        candidate += 1


def word_frequency(text: str) -> dict:
    """
    Count word occurrences in a string (case-insensitive).

    Uses a for loop and the dict.get() pattern.

    Args:
        text: A plain-text string.

    Returns:
        A dict mapping each unique word (lowercase) to its count.
    """
    frequency: dict[str, int] = {}
    for word in text.lower().split():
        # Strip punctuation from either end
        clean = word.strip(".,!?;:\"'()-")
        if clean:
            frequency[clean] = frequency.get(clean, 0) + 1
    return frequency


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    print("=" * 45)
    print("  Exercise 3 – Loops")
    print("=" * 45)
    print()

    # Multiples
    result = sum_of_multiples(1000, 3, 5)
    print(f"Sum of multiples of 3 or 5 below 1000 : {result}")
    print()

    # Countdown
    print("Countdown from 5:")
    print(" ", countdown(5))
    print()

    # Flatten
    nested_lists = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
    print(f"Flatten {nested_lists}")
    print("  →", flatten(nested_lists))
    print()

    # Multiplication table (4×4)
    size = 4
    table = multiplication_table(size)
    print(f"{size}×{size} Multiplication Table:")
    for row in table:
        print(" ", "  ".join(f"{val:2}" for val in row))
    print()

    # First prime above
    for base in [10, 20, 50, 100]:
        print(f"First prime above {base:>3} → {first_prime_above(base)}")
    print()

    # Word frequency
    sample = "to be or not to be that is the question"
    freq = word_frequency(sample)
    sorted_freq = sorted(freq.items(), key=lambda kv: kv[1], reverse=True)
    print(f'Word frequency in "{sample}":')
    for word, count in sorted_freq:
        print(f"  {word:<12} : {count}")
