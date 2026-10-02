"""
modules_utils.py
----------------
A small helper module imported by modules_exercise.py.

This file exists purely to show how you can split related utilities
into a separate module and import them elsewhere.
"""

import re


def celsius_to_fahrenheit(celsius: float) -> float:
    """
    Convert Celsius to Fahrenheit.

    Formula: F = (C × 9/5) + 32

    Args:
        celsius: Temperature in degrees Celsius.

    Returns:
        Equivalent temperature in degrees Fahrenheit.
    """
    return (celsius * 9 / 5) + 32


def is_palindrome(word: str) -> bool:
    """
    Return True if `word` reads the same forwards and backwards
    (case-insensitive).

    Args:
        word: Any string.

    Returns:
        bool
    """
    cleaned = word.lower().replace(" ", "")
    return cleaned == cleaned[::-1]


def slugify(text: str) -> str:
    """
    Convert a human-readable title into a URL-friendly slug.

    Steps:
        1. Lowercase the text.
        2. Replace spaces and non-alphanumeric characters with hyphens.
        3. Strip leading/trailing hyphens.
        4. Collapse consecutive hyphens.

    Args:
        text: The title string to convert.

    Returns:
        A slug string, e.g. 'hello-world'.

    Example:
        slugify("Hello World!") → 'hello-world'
    """
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s-]", "", text)   # remove non-alphanumeric
    text = re.sub(r"[\s-]+", "-", text)          # spaces/hyphens → single hyphen
    return text.strip("-")
