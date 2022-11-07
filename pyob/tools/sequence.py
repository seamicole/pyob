# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ GENERAL IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from typing import overload

# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ PROJECT IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from pyob.tools.check import is_sequence
from pyob.types import Sequence


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ DEDUPLICATE
# └─────────────────────────────────────────────────────────────────────────────────────


@overload
def deduplicate(sequence: list, recurse: bool = False) -> list:
    ...


@overload
def deduplicate(sequence: set, recurse: bool = False) -> set:
    ...


@overload
def deduplicate(sequence: tuple, recurse: bool = False) -> tuple:
    ...


def deduplicate(sequence: Sequence, recurse: bool = False) -> Sequence:
    """Removes duplcates from an iterable while preserving its order"""

    # Determine sequence cast function
    # i.e. The callable type of the passed in sequence
    to_type = type(sequence)

    # Initialize seen set
    # i.e. The set we use to identify diplicate items
    seen = set()
    see = seen.add

    # Remove duplicates items from sequence
    sequence = [
        deduplicate(i, recurse=recurse) if recurse and is_sequence(i) else i
        for i in sequence
        if is_sequence(i) or not (i in seen or see(i))
    ]

    # Return sequence of unique items
    return to_type(sequence)
