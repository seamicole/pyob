# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ GENERAL IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from __future__ import annotations

from typing import Sequence, TYPE_CHECKING

# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ PROJECT IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

if TYPE_CHECKING:
    from pyob.types import HashableSequence


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ FREEZESET
# └─────────────────────────────────────────────────────────────────────────────────────


def freezeset(sequence: HashableSequence) -> frozenset:
    """Recursively converts a hashable sequence into a frozenset"""

    # Return frozen set of the hashable sequence
    return frozenset(
        [
            freezeset(element)
            if isinstance(element, Sequence) and not isinstance(element, str)
            else element
            for element in sequence
        ]
    )
