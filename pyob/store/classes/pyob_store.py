# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ GENERAL IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ PROJECT IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from pyob.utils.mixins.pyobs import PyObs

if TYPE_CHECKING:
    from pyob.types import PyOb


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ PYOB STORE
# └─────────────────────────────────────────────────────────────────────────────────────

# Define a PyOb TypeVar
PyObVar = TypeVar("PyObVar", bound="PyOb")


class PyObStore(PyObs[PyObVar]):
    """An abstract class for a primary collection of PyObClass instances"""

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ TYPE DECLARATION: COUNTS
    # └─────────────────────────────────────────────────────────────────────────────────

    # Declare type of counts
    _counts: dict[PyObVar, int]

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ __ADD__
    # └─────────────────────────────────────────────────────────────────────────────────

    def __add__(self, item: PyObVar) -> PyObStore[PyObVar]:
        """Add Method"""

        # Add PyOb instance to counts
        self._counts[item] = 1

        # Return PyOb store
        return self

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ __SUB__
    # └─────────────────────────────────────────────────────────────────────────────────

    def __sub__(self, item: PyObVar) -> PyObStore[PyObVar]:
        """Subtract Method"""

        # Remove PyOb instance from counts
        self._counts.pop(item, None)

        # Return PyOb store
        return self
