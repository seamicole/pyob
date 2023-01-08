# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ GENERAL IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from __future__ import annotations

from typing import Generic, TYPE_CHECKING, TypeVar

# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ PROJECT IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from pyob.utils.classes.sequence import FrozenDict
from pyob.utils.mixins.pyobs import PyObs

if TYPE_CHECKING:
    from pyob.types import PyOb


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ PYOB SET
# └─────────────────────────────────────────────────────────────────────────────────────

# Define a PyOb TypeVar
PyObInstance = TypeVar("PyObInstance", bound="PyOb")


class PyObSet(PyObs[PyObInstance], Generic[PyObInstance]):
    """An abstract class for a collection of PyOb instances"""

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ CLASS ATTRIBUTES
    # └─────────────────────────────────────────────────────────────────────────────────

    # Declare type of counts
    _counts: FrozenDict[PyObInstance, int]

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ __ADD__
    # └─────────────────────────────────────────────────────────────────────────────────

    def __add__(self, other: PyObInstance) -> PyObSet[PyObInstance]:
        """Add Method"""

        # Return PyOb set
        return self

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ __INIT__
    # └─────────────────────────────────────────────────────────────────────────────────

    def __init__(
        self,
        _counts: dict[PyObInstance, int] | FrozenDict[PyObInstance, int] | None = None,
    ) -> None:
        """Init Method"""

        # Initialize counts
        _counts = _counts or {}

        # Compute length as sum of counts
        _length = sum(_counts.values())

        # Check if the sum of counts is less than the number of PyObs
        # Because any PyObs with a count of zero and should be removed
        if _length < len(_counts):

            # Remove all PyObs with a count of zero
            _counts = {pyob: count for pyob, count in _counts.items() if count > 0}

            # Re-compute length as sum of counts
            _length = sum(_counts.values())

        # Ensure that counts is a FrozenDict
        # A PyObSet should be considered immutable
        _counts = _counts if type(_counts) is FrozenDict else FrozenDict(_counts)

        # Set counts attribute
        self._counts = _counts

        # Set length attribute
        self._length = _length

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ __SUB__
    # └─────────────────────────────────────────────────────────────────────────────────

    def __sub__(self, other: PyObInstance) -> PyObSet[PyObInstance]:
        """Subtract Method"""

        # Return PyOb set
        return self
