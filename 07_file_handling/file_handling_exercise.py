"""
Exercise 7: File Handling
=========================
Topics covered:
  - Reading text files line-by-line
  - Writing and appending to text files
  - Using the `with` statement (context manager)
  - Working with CSV files via the csv module
  - Working with JSON files via the json module
  - pathlib.Path for modern, cross-platform paths
"""

import csv
import json
import os
from pathlib import Path


# All sample files live next to this script
DATA_DIR = Path(__file__).parent / "data"


def ensure_data_dir() -> None:
    """Create the ./data/ directory if it does not already exist."""
    DATA_DIR.mkdir(exist_ok=True)


# ---------------------------------------------------------------------------
# 7-A  Plain text files
# ---------------------------------------------------------------------------
def write_poem(filename: str, lines: list[str]) -> Path:
    """
    Write a list of lines to a text file, one line per row.

    Args:
        filename: Name of the file (within DATA_DIR).
        lines:    Lines to write.

    Returns:
        Resolved Path to the created file.
    """
    ensure_data_dir()
    filepath = DATA_DIR / filename
    with open(filepath, "w", encoding="utf-8") as f:
        for line in lines:
            f.write(line + "\n")
    print(f"  Written: {filepath}")
    return filepath


def read_poem(filepath: Path) -> list[str]:
    """
    Read a text file and return each line as a list item (stripped).

    Args:
        filepath: Path to the file.

    Returns:
        List of stripped lines.
    """
    with open(filepath, encoding="utf-8") as f:
        return [line.rstrip("\n") for line in f]


def append_to_poem(filepath: Path, extra_lines: list[str]) -> None:
    """
    Append additional lines to an existing text file.

    Args:
        filepath:    Path to the file.
        extra_lines: Lines to append.
    """
    with open(filepath, "a", encoding="utf-8") as f:
        for line in extra_lines:
            f.write(line + "\n")
    print(f"  Appended {len(extra_lines)} lines to {filepath.name}")


# ---------------------------------------------------------------------------
# 7-B  CSV files
# ---------------------------------------------------------------------------
def write_students_csv(filename: str, students: list[dict]) -> Path:
    """
    Write a list of student dicts to a CSV file.

    Args:
        filename: File name within DATA_DIR.
        students: List of dicts with keys: name, grade, score.

    Returns:
        Path to the written file.
    """
    ensure_data_dir()
    filepath = DATA_DIR / filename
    fieldnames = ["name", "grade", "score"]

    with open(filepath, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(students)

    print(f"  Written CSV: {filepath}")
    return filepath


def read_students_csv(filepath: Path) -> list[dict]:
    """
    Read student records from a CSV file.

    Converts the 'score' field to float.

    Args:
        filepath: Path to the CSV file.

    Returns:
        List of dicts with score as float.
    """
    students = []
    with open(filepath, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            row["score"] = float(row["score"])
            students.append(dict(row))
    return students


# ---------------------------------------------------------------------------
# 7-C  JSON files
# ---------------------------------------------------------------------------
def save_config(filename: str, config: dict) -> Path:
    """
    Serialise a configuration dict to a JSON file.

    Args:
        filename: File name within DATA_DIR.
        config:   The configuration dictionary.

    Returns:
        Path to the written file.
    """
    ensure_data_dir()
    filepath = DATA_DIR / filename

    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(config, f, indent=2)

    print(f"  Saved JSON: {filepath}")
    return filepath


def load_config(filepath: Path) -> dict:
    """
    Load a JSON file and return it as a Python dict.

    Args:
        filepath: Path to the JSON file.

    Returns:
        Parsed config dictionary.
    """
    with open(filepath, encoding="utf-8") as f:
        return json.load(f)


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    print("=" * 45)
    print("  Exercise 7 – File Handling")
    print("=" * 45)
    print()

    # --- Text file ---
    print("--- Plain Text ---")
    poem_lines = [
        "Shall I compare thee to a summer's day?",
        "Thou art more lovely and more temperate:",
        "Rough winds do shake the darling buds of May,",
        "And summer's lease hath all too short a date.",
    ]
    poem_path = write_poem("sonnet18.txt", poem_lines)
    append_to_poem(poem_path, ["", "  — William Shakespeare, Sonnet 18"])
    content = read_poem(poem_path)
    print(f"\n  Contents of {poem_path.name}:")
    for line in content:
        print(f"    {line}")
    print()

    # --- CSV ---
    print("--- CSV ---")
    students = [
        {"name": "Alice",   "grade": "A", "score": 94.5},
        {"name": "Bob",     "grade": "B", "score": 83.0},
        {"name": "Charlie", "grade": "C", "score": 71.5},
        {"name": "Diana",   "grade": "A", "score": 97.0},
    ]
    csv_path = write_students_csv("students.csv", students)
    loaded = read_students_csv(csv_path)
    print("\n  Loaded student records:")
    for s in loaded:
        print(f"    {s['name']:<10} grade={s['grade']}  score={s['score']}")
    top_student = max(loaded, key=lambda s: s["score"])
    print(f"\n  Top student: {top_student['name']} ({top_student['score']})")
    print()

    # --- JSON ---
    print("--- JSON ---")
    app_config = {
        "app_name": "PythonFundamentals",
        "version": "1.0.0",
        "debug": False,
        "max_retries": 3,
        "allowed_hosts": ["localhost", "127.0.0.1"],
    }
    json_path = save_config("config.json", app_config)
    loaded_config = load_config(json_path)
    print(f"\n  Loaded config: {loaded_config}")
