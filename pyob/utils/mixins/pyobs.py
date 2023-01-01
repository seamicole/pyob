# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ GENERAL IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from __future__ import annotations

from typing import Generic, TYPE_CHECKING, TypeVar

# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ PROJECT IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

if TYPE_CHECKING:
    from pyob.types import FrozenDict, PyObInstance


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ PYOBS MIXIN
# └─────────────────────────────────────────────────────────────────────────────────────

# Define a PyObInstance TypeVar
PyObInstanceVar = TypeVar("PyObInstanceVar", bound="PyObInstance")


class PyObsMixin(Generic[PyObInstanceVar]):
    """An abstract class with methods for handling a collection of PyOb instances"""

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ TYPE DECLARATION: COUNTS
    # └─────────────────────────────────────────────────────────────────────────────────

    # Declare type of counts
    _counts: dict[PyObInstanceVar, int] | "FrozenDict"[PyObInstanceVar, int]

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ TYPE DECLARATION: LENGTH
    # └─────────────────────────────────────────────────────────────────────────────────

    # Declare type of length
    _length: int

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ __ADD__
    # └─────────────────────────────────────────────────────────────────────────────────

    def __add__(self, other: PyObInstance) -> None:
        """Add Method"""

        # Raise NotImplementedError
        raise NotImplementedError

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ __INIT__
    # └─────────────────────────────────────────────────────────────────────────────────

    def __init__(self, _counts: dict[PyObInstanceVar, int] | None = None) -> None:
        """Init Method"""

        # Initialize counts dictionary
        self._counts = _counts or {}

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
    # │ __SUB__
    # └─────────────────────────────────────────────────────────────────────────────────

    def __sub__(self, other: PyObInstance) -> None:
        """Subtract Method"""

        # Raise NotImplementedError
        raise NotImplementedError

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ COUNT
    # └─────────────────────────────────────────────────────────────────────────────────

    def count(self) -> int:
        """Return length of pyob set"""

        # Return length
        return self.__len__()

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ LENGTH
    # └─────────────────────────────────────────────────────────────────────────────────

    @property
    def length(self) -> int:
        """Returns length of pyob set"""

        # Return length
        return self.__len__()
