# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ GENERAL IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from __future__ import annotations

from typing import Generic, Literal, TYPE_CHECKING, TypeVar

# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ PROJECT IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

if TYPE_CHECKING:
    from pyob.types import FrozenDict, PyOb


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ PYOBS
# └─────────────────────────────────────────────────────────────────────────────────────

# Define a PyOb instance TypeVar
PyObInstance = TypeVar("PyObInstance", bound="PyOb")


class PyObs(Generic[PyObInstance]):
    """An abstract class with methods for handling a collection of PyOb instances"""

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ TYPE VARIABLE: SELF
    # └─────────────────────────────────────────────────────────────────────────────────

    # Define a self TypeVar
    Self = TypeVar("Self", bound="PyObs[PyObInstance]")

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ TYPE DECLARATION: COUNTS
    # └─────────────────────────────────────────────────────────────────────────────────

    # Declare type of counts
    _counts: dict[PyObInstance, Literal[1]] | "FrozenDict"[PyObInstance, int]

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ TYPE DECLARATION: LENGTH
    # └─────────────────────────────────────────────────────────────────────────────────

    # Declare type of length
    _length: int

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ __ADD__
    # └─────────────────────────────────────────────────────────────────────────────────

    def __add__(self: Self, item: PyObInstance) -> Self:
        """Add Method"""

        # Raise NotImplementedError
        raise NotImplementedError

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

    def __sub__(self: Self, item: PyObInstance) -> Self:
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
