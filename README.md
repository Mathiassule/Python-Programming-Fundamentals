# Python Programming Fundamentals

A well-organised collection of Python exercises grouped by core language concept.  
Each folder contains a self-contained script that can be run directly, and two exercises  
include a full automated test suite (pytest).

---

## 📂 Repository Structure

```
Python-Programming-Fundamentals/
│
├── 01_variables_and_data_types/
│   └── variables_exercise.py        # Data types, type casting, f-strings, stats
│
├── 02_conditionals/
│   └── conditionals_exercise.py     # Grade calc, BMI, FizzBuzz, ticket pricing
│
├── 03_loops/
│   └── loops_exercise.py            # Multiples, countdown, flatten, primes, word freq
│
├── 04_functions/
│   └── functions_exercise.py        # Defaults, *args, **kwargs, recursion, closures
│
├── 05_modules/
│   ├── modules_exercise.py          # math, random, datetime, Counter, custom module
│   └── modules_utils.py             # Helper module (celsius, palindrome, slugify)
│
├── 06_error_handling/
│   └── error_handling_exercise.py   # Custom exceptions, BankAccount, try/finally
│
├── 07_file_handling/
│   ├── file_handling_exercise.py    # Text, CSV, JSON files; pathlib
│   └── data/                        # Created at runtime (gitignored)
│
├── 08_script_organisation/
│   └── script_organisation_exercise.py  # argparse CLI, logging, layered design
│
├── tests/
│   ├── conftest.py
│   ├── test_functions_exercise.py       # ✅ Automated tests – Exercise 4
│   └── test_error_handling_exercise.py  # ✅ Automated tests – Exercise 6
│
├── DEBUGGING_NOTE.md
├── requirements.txt
└── README.md
```

---

## ⚡ Quick Start

### 1 – Clone the repository

```bash
git clone https://github.com/<your-username>/Python-Programming-Fundamentals.git
cd Python-Programming-Fundamentals
```

### 2 – Create and activate a virtual environment

**Windows (PowerShell):**
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**macOS / Linux:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3 – Install dependencies

```bash
pip install -r requirements.txt
```

> The only runtime dependency is **pytest** (for running the automated tests).  
> All exercises otherwise use the Python standard library only.

---

## ▶️ Running the Exercises

Each exercise is a standalone script. Run them from the repo root like this:

| Exercise | Command |
|---|---|
| 01 – Variables & Data Types | `python 01_variables_and_data_types/variables_exercise.py` |
| 02 – Conditionals | `python 02_conditionals/conditionals_exercise.py` |
| 03 – Loops | `python 03_loops/loops_exercise.py` |
| 04 – Functions | `python 04_functions/functions_exercise.py` |
| 05 – Modules | `python 05_modules/modules_exercise.py` |
| 06 – Error Handling | `python 06_error_handling/error_handling_exercise.py` |
| 07 – File Handling | `python 07_file_handling/file_handling_exercise.py` |
| 08 – Script Organisation | `python 08_script_organisation/script_organisation_exercise.py` |

### CLI mode (Exercise 8)

The script organisation exercise doubles as a real CLI tool:

```bash
# Convert 5 km to miles
python 08_script_organisation/script_organisation_exercise.py 5 km miles

# Show all conversions for 26.2 miles (marathon)
python 08_script_organisation/script_organisation_exercise.py --all 26.2 miles

# Get help
python 08_script_organisation/script_organisation_exercise.py --help
```

---

## ✅ Running the Automated Tests

Run **all** tests from the repo root:

```bash
python -m pytest tests/ -v
```

Run a single test file:

```bash
python -m pytest tests/test_functions_exercise.py -v
python -m pytest tests/test_error_handling_exercise.py -v
```

Run with a coverage report (requires `pytest-cov`):

```bash
pip install pytest-cov
python -m pytest tests/ --cov=. --cov-report=term-missing -v
```

### Expected test output

```
tests/test_functions_exercise.py::TestGreet::test_default_greeting        PASSED
tests/test_functions_exercise.py::TestGreet::test_custom_greeting          PASSED
...
tests/test_error_handling_exercise.py::TestBankAccountHappyPath::...       PASSED
...
========== 40+ passed in 0.XX seconds ==========
```

---

## 🧩 Exercise Summaries

### 01 – Variables and Data Types
- Describes a person using multiple data types (`str`, `int`, `float`, `bool`).
- Demonstrates common type conversions (`int()`, `float()`, `str()`, `bool()`).
- Computes basic statistics (count, sum, mean, min, max) over a list.

### 02 – Conditionals
- **Grade calculator** – converts numeric scores to letter grades (A–F).
- **BMI categoriser** – classifies BMI using the WHO scale.
- **FizzBuzz** – classic divisibility exercise with correct ordering.
- **Ticket pricing** – applies multiple conditions including membership discount.

### 03 – Loops
- Sums multiples of 3 or 5 below 1000 using a generator expression.
- Builds a countdown sequence with a `while` loop.
- Flattens a list-of-lists with nested `for` loops.
- Generates an n×n multiplication table as a 2-D list comprehension.
- Finds the first prime above *n* using a `while True` / `break` pattern.
- Counts word frequencies with `dict.get()` inside a `for` loop.

### 04 – Functions  *(tested)*
- Default parameters, `*args`, `**kwargs`.
- Recursive `fibonacci()` and `factorial()`.
- Higher-order functions: `apply_twice()` and `make_multiplier()` (closure/factory).

### 05 – Modules
- Standard library: `math`, `random`, `datetime`, `collections.Counter`.
- Custom helper module (`modules_utils.py`) with `celsius_to_fahrenheit()`,  
  `is_palindrome()`, and `slugify()`.

### 06 – Error Handling  *(tested)*
- Custom exception hierarchy: `BankError → InsufficientFundsError / NegativeAmountError`.
- `BankAccount` class demonstrating `try / except / finally`.
- `safe_parse_int()` – graceful handling of invalid user input.
- `read_first_line()` – `finally` block guarantees file closure.

### 07 – File Handling
- Reads/writes/appends plain text files with `open()` and context managers.
- Writes and reads CSV files using `csv.DictWriter` / `csv.DictReader`.
- Serialises and deserialises JSON configs with `json.dump()` / `json.load()`.
- Uses `pathlib.Path` throughout for cross-platform compatibility.

### 08 – Script Organisation
- **Distance unit converter** with a full CLI (`argparse`).
- Separated into distinct layers: constants → business logic → presentation → CLI.
- Uses `logging` instead of raw `print()` for diagnostic messages.
- Demonstrates the `if __name__ == "__main__"` entry-point pattern.

---

## 🐍 Python Version

Developed and tested on **Python 3.11+**.  
Uses union-type hints (`int | None`) which require Python ≥ 3.10.

---

## 📝 Debugging Note

See [`DEBUGGING_NOTE.md`](DEBUGGING_NOTE.md) for a detailed account of one error  
encountered during development, its root cause, and the fix applied.
