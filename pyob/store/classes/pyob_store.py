# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ GENERAL IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from __future__ import annotations

from typing import Literal, TYPE_CHECKING, TypeVar

# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ PROJECT IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from pyob.utils.mixins.pyobs import PyObs

if TYPE_CHECKING:
    from pyob.types import PyOb


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ PYOB STORE
# └─────────────────────────────────────────────────────────────────────────────────────

# Define a PyOb instance TypeVar
PyObInstance = TypeVar("PyObInstance", bound="PyOb")


class PyObStore(PyObs[PyObInstance]):
    """An abstract class for a primary collection of PyObClass instances"""

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ TYPE DECLARATION: COUNTS
    # └─────────────────────────────────────────────────────────────────────────────────

    # Declare type of counts
    _counts: dict[PyObInstance, Literal[1]]

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ __INIT__
    # └─────────────────────────────────────────────────────────────────────────────────

    def __init__(self) -> None:
        """Init Method"""

        # Set counts attribute
        self._counts = {}

        # Set length attribute
        self._length = 0

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ STORE
    # └─────────────────────────────────────────────────────────────────────────────────

    def store(self, item: PyObInstance) -> PyObStore[PyObInstance]:
        """Adds a PyOb instance to the PyOb store"""

        # Add PyOb instance to counts
        self._counts[item] = 1

        # Return PyOb store
        return self

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ UNSTORE
    # └─────────────────────────────────────────────────────────────────────────────────

    def unstore(self, item: PyObInstance) -> PyObStore[PyObInstance]:
        """Removes a PyOb instance from the PyOb store"""

        # Pop PyOb instance from counts
        self._counts.pop(item, None)

        # Return PyOb store
        return self
