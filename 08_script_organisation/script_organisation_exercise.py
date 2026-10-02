"""
Exercise 8: Script Organisation
================================
Topics covered:
  - Structuring a real-world CLI application
  - Separating concerns: data, logic, and presentation layers
  - Using argparse for command-line interfaces
  - __name__ == '__main__' guard
  - Constants, type hints, and clear module-level docstrings
  - Logging instead of print() for diagnostic output
"""

import argparse
import logging
import sys

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------
SUPPORTED_UNITS = ("km", "miles", "m", "ft")
CONVERSION_TABLE: dict[tuple[str, str], float] = {
    ("km",    "miles"): 0.621371,
    ("miles", "km"):    1.60934,
    ("m",     "ft"):    3.28084,
    ("ft",    "m"):     0.3048,
    ("km",    "m"):     1000.0,
    ("m",     "km"):    0.001,
    ("miles", "ft"):    5280.0,
    ("ft",    "miles"): 0.000189394,
}

# ---------------------------------------------------------------------------
# Logging setup (separate from print / user output)
# ---------------------------------------------------------------------------
logging.basicConfig(
    level=logging.DEBUG,
    format="%(levelname)-8s | %(message)s",
)
logger = logging.getLogger(__name__)


# ---------------------------------------------------------------------------
# Data / business-logic layer
# ---------------------------------------------------------------------------
def convert_distance(value: float, from_unit: str, to_unit: str) -> float:
    """
    Convert a distance value between two units.

    Supported units: km, miles, m, ft.

    Args:
        value:     Numeric distance to convert (must be ≥ 0).
        from_unit: Source unit (e.g. 'km').
        to_unit:   Target unit (e.g. 'miles').

    Returns:
        Converted distance as a float.

    Raises:
        ValueError: if a unit is unsupported or the pair has no direct
                    conversion defined.
        ValueError: if value is negative.
    """
    from_unit = from_unit.lower().strip()
    to_unit   = to_unit.lower().strip()

    if value < 0:
        raise ValueError(f"Distance cannot be negative; got {value}.")

    if from_unit not in SUPPORTED_UNITS:
        raise ValueError(f"Unknown unit: {from_unit!r}. Choose from {SUPPORTED_UNITS}.")

    if to_unit not in SUPPORTED_UNITS:
        raise ValueError(f"Unknown unit: {to_unit!r}. Choose from {SUPPORTED_UNITS}.")

    if from_unit == to_unit:
        logger.debug("Same unit – no conversion needed.")
        return value

    key = (from_unit, to_unit)
    if key not in CONVERSION_TABLE:
        raise ValueError(
            f"No direct conversion from {from_unit!r} → {to_unit!r}. "
            f"Supported pairs: {list(CONVERSION_TABLE.keys())}"
        )

    factor = CONVERSION_TABLE[key]
    result = value * factor
    logger.debug("Converting %.4f %s → %.4f %s (factor=%.6f)",
                 value, from_unit, result, to_unit, factor)
    return result


def batch_convert(values: list[float], from_unit: str, to_unit: str) -> list[float]:
    """
    Convert a list of distances in one call.

    Args:
        values:    List of numeric distances.
        from_unit: Source unit.
        to_unit:   Target unit.

    Returns:
        List of converted values in the same order.
    """
    return [convert_distance(v, from_unit, to_unit) for v in values]


# ---------------------------------------------------------------------------
# Presentation layer
# ---------------------------------------------------------------------------
def display_conversion(value: float, from_unit: str, to_unit: str) -> None:
    """Print a single conversion in a user-friendly format."""
    result = convert_distance(value, from_unit, to_unit)
    print(f"  {value} {from_unit}  =  {result:.4f} {to_unit}")


def display_all_conversions(value: float, from_unit: str) -> None:
    """
    Show conversions from `from_unit` to every other supported unit.

    Args:
        value:     The source distance.
        from_unit: The unit to convert from.
    """
    print(f"\n  Conversions for {value} {from_unit}:")
    for (src, tgt), _ in CONVERSION_TABLE.items():
        if src == from_unit:
            result = convert_distance(value, src, tgt)
            print(f"    → {result:.4f} {tgt}")


# ---------------------------------------------------------------------------
# CLI layer (argparse)
# ---------------------------------------------------------------------------
def build_parser() -> argparse.ArgumentParser:
    """Construct and return the CLI argument parser."""
    parser = argparse.ArgumentParser(
        prog="unit_converter",
        description="Convert distances between km, miles, m, and ft.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "Examples:\n"
            "  python script_organisation_exercise.py 5 km miles\n"
            "  python script_organisation_exercise.py 100 m ft\n"
            "  python script_organisation_exercise.py --all 26.2 miles\n"
        ),
    )
    parser.add_argument("value",     type=float, help="Distance to convert.")
    parser.add_argument("from_unit", type=str,   help="Source unit (km/miles/m/ft).")
    parser.add_argument(
        "to_unit",
        type=str,
        nargs="?",
        help="Target unit. Omit with --all to show all conversions.",
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="Show conversions to all available units.",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    """
    Entry point for the CLI.

    Args:
        argv: Argument list (uses sys.argv if None).

    Returns:
        Exit code (0 = success, 1 = error).
    """
    parser = build_parser()
    args = parser.parse_args(argv)

    try:
        if args.all:
            display_all_conversions(args.value, args.from_unit)
        elif args.to_unit:
            display_conversion(args.value, args.from_unit, args.to_unit)
        else:
            parser.error("Provide a to_unit or use --all.")
    except ValueError as exc:
        logger.error(exc)
        return 1

    return 0


# ---------------------------------------------------------------------------
# __name__ guard – this is the standard Python entry-point pattern
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    # Demo mode: run a set of conversions without needing CLI args
    print("=" * 45)
    print("  Exercise 8 – Script Organisation")
    print("=" * 45)
    print()
    print("  Unit Converter – demo mode")
    print("  (Run with --help for CLI usage)")
    print()

    demo_conversions = [
        (42.195, "km",    "miles"),   # marathon distance
        (100.0,  "miles", "km"),
        (1.8288, "m",     "ft"),      # 6 feet
        (5280.0, "ft",    "miles"),   # 1 mile
    ]

    for val, frm, to in demo_conversions:
        display_conversion(val, frm, to)

    print()
    display_all_conversions(10, "km")

    # Trigger error-handling path
    print("\n  Attempting negative distance …")
    exit_code = main(["−5", "km", "miles"])
    sys.exit(exit_code)
