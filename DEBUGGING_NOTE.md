# Debugging Note

> **Exercise affected:** Exercise 6 – Error Handling  
> **File affected:** `06_error_handling/error_handling_exercise.py`

---

## The Error

When first running the test suite against `BankAccount`, the following test failed:

```
FAILED tests/test_error_handling_exercise.py::TestBankAccountExceptions::test_balance_unchanged_after_failed_deposit
AssertionError: assert 60.0 == 50.0
```

The test expected the balance to remain **£50.00** after a failed deposit,  
but it was reading **£60.00** — meaning the deposit of `-£10.00` had been  
applied before the validation ran.

---

## The Root Cause

The original `deposit()` method was written like this:

```python
def deposit(self, amount: float) -> None:
    self._balance += amount          # ← balance mutated FIRST
    if amount <= 0:
        raise NegativeAmountError(amount)   # ← check happens AFTER
    self._history.append(...)
```

Because Python executes statements top-to-bottom, the balance was  
incremented **before** the guard clause checked whether the amount was  
valid. When the exception was raised the mutation had already occurred,  
leaving the account in a corrupted state.

---

## The Fix

The fix was simply to **move the validation check above any state mutation** —  
a classic "guard clause first" pattern:

```python
def deposit(self, amount: float) -> None:
    if amount <= 0:                  # ← validate FIRST
        raise NegativeAmountError(amount)
    self._balance += amount          # ← only mutate after passing validation
    self._history.append(...)
```

The same fix was applied symmetrically to `withdraw()`.

---

## What I Learned

> **Validate inputs before mutating state.**  
> If a function changes an object's internal state, all validation should  
> happen at the very top of the function body — before any assignments or  
> appends. This ensures that a raised exception always leaves the object  
> exactly as it was found (an "atomic" operation).

This is closely related to the software design principle of  
**fail-fast**: detect invalid conditions as early as possible and signal  
them immediately, rather than discovering problems after partial work has  
been done.

---

## How the Test Caught It

The test `test_balance_unchanged_after_failed_deposit` deliberately triggers  
the error path and then asserts the balance is unchanged:

```python
def test_balance_unchanged_after_failed_deposit(self):
    acc = BankAccount("Test User", initial_balance=50.0)
    with pytest.raises(NegativeAmountError):
        acc.deposit(-10.0)
    assert acc.balance == 50.0   # must be unchanged
```

Without this test the bug would have been invisible: the `NegativeAmountError`  
was still raised (so the caller saw the right exception), but the internal  
balance was silently corrupted — a subtle data-integrity bug.
