"""
tests/test_functions_exercise.py
================================
Automated tests for Exercise 4: Functions.

Run with:
    python -m pytest tests/test_functions_exercise.py -v
or from the repo root:
    python -m pytest -v
"""

import sys
import os
import pytest

# Make sure Python can find the exercise module
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "04_functions"))

from functions_exercise import (
    greet,
    total_cost,
    build_profile,
    fibonacci,
    factorial,
    apply_twice,
    make_multiplier,
)


# ---------------------------------------------------------------------------
# greet()
# ---------------------------------------------------------------------------
class TestGreet:
    def test_default_greeting(self):
        assert greet("World") == "Hello, World!"

    def test_custom_greeting(self):
        assert greet("Alice", greeting="Hi") == "Hi, Alice!"

    def test_custom_punctuation(self):
        assert greet("Bob", punctuation=".") == "Hello, Bob."

    def test_all_custom(self):
        result = greet("Eve", greeting="Good evening", punctuation="~")
        assert result == "Good evening, Eve~"

    def test_empty_name(self):
        # An empty name is unusual but should not raise an exception
        assert greet("") == "Hello, !"


# ---------------------------------------------------------------------------
# total_cost()
# ---------------------------------------------------------------------------
class TestTotalCost:
    def test_single_item_default_tax(self):
        # 10.00 * 1.20 = 12.00
        assert total_cost(10.00) == pytest.approx(12.00)

    def test_multiple_items_default_tax(self):
        # (5 + 5 + 10) * 1.20 = 24.00
        assert total_cost(5.00, 5.00, 10.00) == pytest.approx(24.00)

    def test_zero_tax(self):
        assert total_cost(100.00, tax_rate=0.0) == pytest.approx(100.00)

    def test_custom_tax(self):
        # 200 * 1.05 = 210.00
        assert total_cost(200.00, tax_rate=0.05) == pytest.approx(210.00)

    def test_no_items(self):
        # Sum of zero items with default tax = 0.00
        assert total_cost(tax_rate=0.20) == pytest.approx(0.00)

    def test_result_rounded_to_two_places(self):
        # (1/3) * 1.20 ≈ 0.40 (rounded)
        result = total_cost(1 / 3, tax_rate=0.20)
        assert result == round(result, 2)


# ---------------------------------------------------------------------------
# fibonacci()
# ---------------------------------------------------------------------------
class TestFibonacci:
    @pytest.mark.parametrize("n, expected", [
        (0,  0),
        (1,  1),
        (2,  1),
        (3,  2),
        (4,  3),
        (5,  5),
        (6,  8),
        (7,  13),
        (10, 55),
    ])
    def test_known_values(self, n, expected):
        assert fibonacci(n) == expected

    def test_negative_raises_value_error(self):
        with pytest.raises(ValueError, match="non-negative"):
            fibonacci(-1)

    def test_large_index(self):
        # F(20) = 6765 – verifies recursion handles larger inputs
        assert fibonacci(20) == 6765


# ---------------------------------------------------------------------------
# factorial()
# ---------------------------------------------------------------------------
class TestFactorial:
    @pytest.mark.parametrize("n, expected", [
        (0,  1),
        (1,  1),
        (2,  2),
        (3,  6),
        (4,  24),
        (5,  120),
        (10, 3628800),
    ])
    def test_known_values(self, n, expected):
        assert factorial(n) == expected

    def test_negative_raises_value_error(self):
        with pytest.raises(ValueError, match="non-negative"):
            factorial(-3)


# ---------------------------------------------------------------------------
# apply_twice()
# ---------------------------------------------------------------------------
class TestApplyTwice:
    def test_with_lambda_increment(self):
        assert apply_twice(lambda x: x + 1, 5) == 7

    def test_with_lambda_double(self):
        # double(double(3)) = double(6) = 12
        assert apply_twice(lambda x: x * 2, 3) == 12

    def test_with_named_function(self):
        def square(x):
            return x ** 2
        # square(square(2)) = square(4) = 16
        assert apply_twice(square, 2) == 16

    def test_identity_function(self):
        assert apply_twice(lambda x: x, 99) == 99


# ---------------------------------------------------------------------------
# make_multiplier()
# ---------------------------------------------------------------------------
class TestMakeMultiplier:
    def test_double(self):
        double = make_multiplier(2)
        assert double(5) == 10

    def test_triple(self):
        triple = make_multiplier(3)
        assert triple(7) == 21

    def test_fractional_factor(self):
        half = make_multiplier(0.5)
        assert half(10) == pytest.approx(5.0)

    def test_zero_factor(self):
        zero_out = make_multiplier(0)
        assert zero_out(1000) == 0

    def test_factory_creates_independent_closures(self):
        double = make_multiplier(2)
        triple = make_multiplier(3)
        assert double(4) == 8
        assert triple(4) == 12
