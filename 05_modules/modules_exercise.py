"""
Exercise 5: Modules
===================
Topics covered:
  - Using the Python standard library (math, random, datetime, collections)
  - Importing specific names with `from … import`
  - Using aliases (`import … as`)
  - Understanding __name__ == '__main__'
  - Writing a helper module (see utils.py in this folder)
"""

import math
import random
import datetime
from collections import Counter

# Import our own helper module from the same folder
from modules_utils import celsius_to_fahrenheit, is_palindrome, slugify


# ---------------------------------------------------------------------------
# Demonstrations
# ---------------------------------------------------------------------------
def math_demo() -> None:
    """Show off several math module capabilities."""
    print("--- math module ---")
    angle_deg = 45
    angle_rad = math.radians(angle_deg)
    print(f"  math.pi           = {math.pi:.6f}")
    print(f"  math.e            = {math.e:.6f}")
    print(f"  math.sqrt(144)    = {math.sqrt(144)}")
    print(f"  math.log10(1000)  = {math.log10(1000)}")
    print(f"  sin({angle_deg}°) = {math.sin(angle_rad):.4f}")
    print(f"  cos({angle_deg}°) = {math.cos(angle_rad):.4f}")
    print()


def random_demo() -> None:
    """Show off several random module capabilities."""
    random.seed(42)   # Fixed seed → reproducible output
    print("--- random module (seed=42) ---")
    print(f"  random.randint(1, 100)  = {random.randint(1, 100)}")
    print(f"  random.uniform(0, 1)    = {random.uniform(0, 1):.4f}")
    choices = ["rock", "paper", "scissors"]
    print(f"  random.choice(...)      = {random.choice(choices)!r}")
    sample_pool = list(range(1, 50))
    lottery = sorted(random.sample(sample_pool, 6))
    print(f"  Lottery numbers (6/49)  = {lottery}")
    print()


def datetime_demo() -> None:
    """Show off the datetime module."""
    print("--- datetime module ---")
    now = datetime.datetime.now()
    print(f"  Current date/time : {now.strftime('%Y-%m-%d %H:%M:%S')}")
    birthday = datetime.date(1815, 12, 10)   # Ada Lovelace's birthday
    today = datetime.date.today()
    delta = today - birthday
    print(f"  Ada Lovelace's birthday : {birthday}")
    print(f"  Days since her birthday : {delta.days:,}")
    future = today + datetime.timedelta(weeks=4)
    print(f"  Four weeks from today   : {future}")
    print()


def counter_demo() -> None:
    """Show the Counter class from the collections module."""
    print("--- collections.Counter ---")
    text = "the quick brown fox jumps over the lazy dog"
    char_counts = Counter(text.replace(" ", ""))
    word_counts = Counter(text.split())
    most_common_chars = char_counts.most_common(5)
    print(f"  Text: {text!r}")
    print(f"  Top-5 characters: {most_common_chars}")
    repeated_words = {w: c for w, c in word_counts.items() if c > 1}
    print(f"  Words appearing >1 time: {repeated_words}")
    print()


def our_utils_demo() -> None:
    """Use the helper functions we wrote in modules_utils.py."""
    print("--- our modules_utils module ---")
    temps_c = [0, 20, 37, 100]
    for c in temps_c:
        print(f"  {c}°C  →  {celsius_to_fahrenheit(c):.1f}°F")
    print()

    words = ["racecar", "hello", "level", "Python", "madam"]
    for word in words:
        status = "palindrome" if is_palindrome(word) else "not a palindrome"
        print(f"  {word!r:<10} is {status}")
    print()

    titles = ["Hello World", "Python Programming 101", "my-cool article!"]
    for title in titles:
        print(f"  slugify({title!r}) → {slugify(title)!r}")
    print()


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    print("=" * 45)
    print("  Exercise 5 – Modules")
    print("=" * 45)
    print()

    math_demo()
    random_demo()
    datetime_demo()
    counter_demo()
    our_utils_demo()
