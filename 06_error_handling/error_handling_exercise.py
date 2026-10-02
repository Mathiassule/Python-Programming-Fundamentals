"""
Exercise 6: Error Handling
==========================
Topics covered:
  - try / except / else / finally
  - Catching specific exception types
  - Raising exceptions with custom messages
  - Creating custom exception classes
  - Exception chaining (raise … from …)
"""


# ---------------------------------------------------------------------------
# 6-A  Custom exception hierarchy
# ---------------------------------------------------------------------------
class BankError(Exception):
    """Base class for all bank-related errors."""


class InsufficientFundsError(BankError):
    """Raised when a withdrawal exceeds the available balance."""

    def __init__(self, requested: float, available: float) -> None:
        self.requested = requested
        self.available = available
        super().__init__(
            f"Cannot withdraw £{requested:.2f}: "
            f"only £{available:.2f} available."
        )


class NegativeAmountError(BankError):
    """Raised when a monetary amount is zero or negative."""

    def __init__(self, amount: float) -> None:
        super().__init__(
            f"Amount must be positive; received £{amount:.2f}."
        )


# ---------------------------------------------------------------------------
# 6-B  BankAccount class – uses the custom exceptions
# ---------------------------------------------------------------------------
class BankAccount:
    """
    A simple bank account with deposit, withdraw, and history.

    Raises:
        NegativeAmountError:    if deposit or withdrawal ≤ 0.
        InsufficientFundsError: if withdrawal > current balance.
    """

    def __init__(self, owner: str, initial_balance: float = 0.0) -> None:
        if initial_balance < 0:
            raise NegativeAmountError(initial_balance)
        self.owner = owner
        self._balance = initial_balance
        self._history: list[str] = [f"Account opened with £{initial_balance:.2f}"]

    @property
    def balance(self) -> float:
        """Current account balance (read-only)."""
        return self._balance

    def deposit(self, amount: float) -> None:
        """
        Add `amount` to the balance.

        Raises:
            NegativeAmountError: if amount ≤ 0.
        """
        if amount <= 0:
            raise NegativeAmountError(amount)
        self._balance += amount
        self._history.append(f"Deposited  £{amount:>8.2f}  →  Balance: £{self._balance:.2f}")

    def withdraw(self, amount: float) -> None:
        """
        Subtract `amount` from the balance.

        Raises:
            NegativeAmountError:    if amount ≤ 0.
            InsufficientFundsError: if amount > balance.
        """
        if amount <= 0:
            raise NegativeAmountError(amount)
        if amount > self._balance:
            raise InsufficientFundsError(amount, self._balance)
        self._balance -= amount
        self._history.append(f"Withdrew   £{amount:>8.2f}  →  Balance: £{self._balance:.2f}")

    def print_history(self) -> None:
        """Print all transactions to stdout."""
        print(f"\n  Transaction history for {self.owner}:")
        for entry in self._history:
            print(f"    {entry}")
        print()


# ---------------------------------------------------------------------------
# 6-C  Safe integer parsing
# ---------------------------------------------------------------------------
def safe_parse_int(value: str) -> int | None:
    """
    Parse a string as an integer.

    Uses try/except to handle invalid input gracefully instead of crashing.

    Args:
        value: The string to parse.

    Returns:
        The parsed integer, or None if parsing fails.
    """
    try:
        return int(value)
    except ValueError:
        print(f"  [Warning] Could not parse {value!r} as an integer.")
        return None


# ---------------------------------------------------------------------------
# 6-D  File-reading with cleanup (try / finally)
# ---------------------------------------------------------------------------
def read_first_line(filepath: str) -> str:
    """
    Read and return the first line of a file.

    The finally block guarantees the file is always closed, even if an
    exception is raised mid-read.

    Args:
        filepath: Absolute or relative path to the file.

    Returns:
        First line of the file (stripped of newline characters).

    Raises:
        FileNotFoundError: if the file does not exist.
    """
    file_handle = None
    try:
        file_handle = open(filepath, encoding="utf-8")
        first_line = file_handle.readline().rstrip("\n")
        return first_line
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {filepath!r}")
    finally:
        if file_handle is not None:
            file_handle.close()   # always runs, even on error


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    print("=" * 45)
    print("  Exercise 6 – Error Handling")
    print("=" * 45)
    print()

    # --- BankAccount happy path ---
    account = BankAccount("Grace Hopper", initial_balance=500.00)
    account.deposit(150.00)
    account.withdraw(75.00)

    # --- Trigger InsufficientFundsError ---
    print("Attempting to overdraw account …")
    try:
        account.withdraw(1000.00)
    except InsufficientFundsError as exc:
        print(f"  Caught InsufficientFundsError: {exc}")

    # --- Trigger NegativeAmountError ---
    print("Attempting to deposit a negative amount …")
    try:
        account.deposit(-50.00)
    except NegativeAmountError as exc:
        print(f"  Caught NegativeAmountError: {exc}")

    account.print_history()

    # --- Safe parsing ---
    print("Safe integer parsing:")
    test_values = ["42", "3.14", "hello", "100"]
    for v in test_values:
        result = safe_parse_int(v)
        print(f"  parse({v!r}) → {result}")
    print()

    # --- FileNotFoundError ---
    print("Reading a non-existent file …")
    try:
        read_first_line("ghost_file.txt")
    except FileNotFoundError as exc:
        print(f"  Caught FileNotFoundError: {exc}")
