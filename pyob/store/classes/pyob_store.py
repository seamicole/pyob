# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ GENERAL IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ PROJECT IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from pyob.utils.mixins.pyobs import PyObsMixin

if TYPE_CHECKING:
    from pyob.types import PyObInstance


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ PYOB STORE
# └─────────────────────────────────────────────────────────────────────────────────────

# Define a PyObInstance TypeVar
PyObInstanceVar = TypeVar("PyObInstanceVar", bound="PyObInstance")


class PyObStore(PyObsMixin[PyObInstanceVar]):
    """An abstract class for a primary collection of PyObClass instances"""

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ __ADD__
    # └─────────────────────────────────────────────────────────────────────────────────

    def __add__(self, other: PyObInstance) -> None:
        """Add Method"""

        # Add PyOb instance to counts
        self._counts[other] = 1

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ __SUB__
    # └─────────────────────────────────────────────────────────────────────────────────

    def __sub__(self, other: PyObInstance) -> None:
        """Subtract Method"""

        # Remove PyOb instance from counts
        self._counts.pop(other, None)
