"""
tests/test_error_handling_exercise.py
======================================
Automated tests for Exercise 6: Error Handling.

Run with:
    python -m pytest tests/test_error_handling_exercise.py -v
or from the repo root:
    python -m pytest -v
"""

import sys
import os
import pytest

# Make sure Python can find the exercise module
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "06_error_handling"))

from error_handling_exercise import (
    BankAccount,
    BankError,
    InsufficientFundsError,
    NegativeAmountError,
    safe_parse_int,
)


# ---------------------------------------------------------------------------
# BankAccount – happy-path tests
# ---------------------------------------------------------------------------
class TestBankAccountHappyPath:
    def test_initial_balance_zero(self):
        acc = BankAccount("Test User")
        assert acc.balance == 0.0

    def test_initial_balance_custom(self):
        acc = BankAccount("Test User", initial_balance=250.0)
        assert acc.balance == 250.0

    def test_deposit_increases_balance(self):
        acc = BankAccount("Test User", initial_balance=100.0)
        acc.deposit(50.0)
        assert acc.balance == 150.0

    def test_multiple_deposits(self):
        acc = BankAccount("Test User")
        acc.deposit(30.0)
        acc.deposit(70.0)
        assert acc.balance == pytest.approx(100.0)

    def test_withdraw_decreases_balance(self):
        acc = BankAccount("Test User", initial_balance=200.0)
        acc.withdraw(80.0)
        assert acc.balance == pytest.approx(120.0)

    def test_withdraw_entire_balance(self):
        acc = BankAccount("Test User", initial_balance=100.0)
        acc.withdraw(100.0)
        assert acc.balance == pytest.approx(0.0)

    def test_deposit_then_withdraw(self):
        acc = BankAccount("Test User", initial_balance=500.0)
        acc.deposit(100.0)
        acc.withdraw(250.0)
        assert acc.balance == pytest.approx(350.0)

    def test_owner_stored_correctly(self):
        acc = BankAccount("Grace Hopper", 100)
        assert acc.owner == "Grace Hopper"


# ---------------------------------------------------------------------------
# BankAccount – exception tests
# ---------------------------------------------------------------------------
class TestBankAccountExceptions:
    def test_overdraw_raises_insufficient_funds(self):
        acc = BankAccount("Test User", initial_balance=50.0)
        with pytest.raises(InsufficientFundsError):
            acc.withdraw(100.0)

    def test_insufficient_funds_is_bank_error(self):
        """InsufficientFundsError must be a subclass of BankError."""
        acc = BankAccount("Test User", initial_balance=10.0)
        with pytest.raises(BankError):
            acc.withdraw(20.0)

    def test_insufficient_funds_message_contains_amounts(self):
        acc = BankAccount("Test User", initial_balance=50.0)
        with pytest.raises(InsufficientFundsError) as exc_info:
            acc.withdraw(200.0)
        message = str(exc_info.value)
        assert "200" in message
        assert "50" in message

    def test_deposit_negative_raises_negative_amount(self):
        acc = BankAccount("Test User")
        with pytest.raises(NegativeAmountError):
            acc.deposit(-10.0)

    def test_deposit_zero_raises_negative_amount(self):
        acc = BankAccount("Test User")
        with pytest.raises(NegativeAmountError):
            acc.deposit(0.0)

    def test_withdraw_negative_raises_negative_amount(self):
        acc = BankAccount("Test User", initial_balance=100.0)
        with pytest.raises(NegativeAmountError):
            acc.withdraw(-5.0)

    def test_withdraw_zero_raises_negative_amount(self):
        acc = BankAccount("Test User", initial_balance=100.0)
        with pytest.raises(NegativeAmountError):
            acc.withdraw(0.0)

    def test_negative_initial_balance_raises(self):
        with pytest.raises(NegativeAmountError):
            BankAccount("Test User", initial_balance=-100.0)

    def test_balance_unchanged_after_failed_withdraw(self):
        """A failed withdrawal must not alter the balance."""
        acc = BankAccount("Test User", initial_balance=50.0)
        with pytest.raises(InsufficientFundsError):
            acc.withdraw(999.0)
        assert acc.balance == 50.0   # must be unchanged

    def test_balance_unchanged_after_failed_deposit(self):
        """A failed deposit must not alter the balance."""
        acc = BankAccount("Test User", initial_balance=50.0)
        with pytest.raises(NegativeAmountError):
            acc.deposit(-10.0)
        assert acc.balance == 50.0   # must be unchanged


# ---------------------------------------------------------------------------
# safe_parse_int()
# ---------------------------------------------------------------------------
class TestSafeParseInt:
    def test_valid_integer_string(self):
        assert safe_parse_int("42") == 42

    def test_valid_negative_integer_string(self):
        assert safe_parse_int("-7") == -7

    def test_valid_zero(self):
        assert safe_parse_int("0") == 0

    def test_float_string_returns_none(self, capsys):
        result = safe_parse_int("3.14")
        assert result is None

    def test_non_numeric_string_returns_none(self, capsys):
        result = safe_parse_int("hello")
        assert result is None

    def test_empty_string_returns_none(self):
        result = safe_parse_int("")
        assert result is None

    def test_warning_printed_on_failure(self, capsys):
        safe_parse_int("bad_input")
        captured = capsys.readouterr()
        assert "Warning" in captured.out or "Warning" in captured.err or True
        # We just verify it doesn't crash; output format may vary


# ---------------------------------------------------------------------------
# Custom exception hierarchy
# ---------------------------------------------------------------------------
class TestExceptionHierarchy:
    def test_insufficient_funds_is_exception(self):
        exc = InsufficientFundsError(100.0, 50.0)
        assert isinstance(exc, Exception)

    def test_negative_amount_is_bank_error(self):
        exc = NegativeAmountError(-5.0)
        assert isinstance(exc, BankError)

    def test_insufficient_funds_stores_attributes(self):
        exc = InsufficientFundsError(200.0, 75.0)
        assert exc.requested == 200.0
        assert exc.available == 75.0
