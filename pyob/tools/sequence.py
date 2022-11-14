# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ GENERAL IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from __future__ import annotations
from typing import Sequence

# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ PROJECT IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from pyob.types import HashableSequence


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ FREEZESET
# └─────────────────────────────────────────────────────────────────────────────────────


def freezeset(sequence: HashableSequence) -> frozenset:
    """Recursively converts a hashable sequence into a frozenset"""

    # Return frozen set of the hashable sequence
    return frozenset([freezeset(i) if isinstance(i, Sequence) else i for i in sequence])
