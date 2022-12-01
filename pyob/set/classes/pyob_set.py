# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ GENERAL IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from __future__ import annotations

from typing import TYPE_CHECKING

# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ PROJECT IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from pyob.utils.sequence import FrozenDict

if TYPE_CHECKING:
    from pyob.types import PyObInstance


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ PYOB SET
# └─────────────────────────────────────────────────────────────────────────────────────


class PyObSet:
    """An abstract class for a collection of PyOb instances"""

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ TYPE DECLARATION: COUNTS
    # └─────────────────────────────────────────────────────────────────────────────────

    # Declare type of counts
    _counts: FrozenDict[PyObInstance, int]

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ TYPE DECLARATION: LENGTH
    # └─────────────────────────────────────────────────────────────────────────────────

    # Declare type of length
    _length: int

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ __INIT__
    # └─────────────────────────────────────────────────────────────────────────────────

    def __init__(self, _counts: dict[PyObInstance, int] | None = None) -> None:
        """Init Method"""

        # Initialize and freeze counts
        self._counts = FrozenDict(_counts or {})

        # Compute and set length of pyob set
        self._length = sum(self._counts.values())

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ __LEN__
    # └─────────────────────────────────────────────────────────────────────────────────

    def __len__(self) -> int:
        """Length Method"""

        # Return length of pyob set
        return self._length

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ LENGTH
    # └─────────────────────────────────────────────────────────────────────────────────

    @property
    def length(self) -> int:
        """Returns length of pyob set"""

        # Return length
        return self.__len__()

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ COUNT
    # └─────────────────────────────────────────────────────────────────────────────────

    def count(self) -> int:
        """Return length of pyob set"""

        # Return length
        return self.__len__()
