# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ GENERAL IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from __future__ import annotations

from typing import Generic, TYPE_CHECKING, TypeVar

# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ PROJECT IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from pyob.utils.classes.sequence import FrozenDict
from pyob.utils.mixins.pyobs_mixin import PyObsMixin

if TYPE_CHECKING:
    from pyob.types import PyObInstance


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ PYOB SET
# └─────────────────────────────────────────────────────────────────────────────────────

# Define a PyObInstance TypeVar
PyObInstanceVar = TypeVar("PyObInstanceVar", bound="PyObInstance")


class PyObSet(PyObsMixin[PyObInstanceVar], Generic[PyObInstanceVar]):
    """An abstract class for a collection of PyOb instances"""

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ TYPE DECLARATION: COUNTS
    # └─────────────────────────────────────────────────────────────────────────────────

    # Declare type of counts
    _counts: FrozenDict[PyObInstanceVar, int]

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ __INIT__
    # └─────────────────────────────────────────────────────────────────────────────────

    def __init__(self, _counts: dict[PyObInstanceVar, int] | None = None) -> None:
        """Init Method"""

        # Call parent init method
        super().__init__(_counts=_counts)

        # Freeze the PyObSet counts dictionary
        # A PyObSet should be considered immutable
        self._counts = FrozenDict(self._counts)
