# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ GENERAL IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from __future__ import annotations

from typing import Literal, TYPE_CHECKING, TypeVar

# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ PROJECT IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from pyob.utils.exceptions.validation import InvalidTypeError, UnexpectedTypeError
from pyob.utils.functions.validators import is_pyob_instance
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
    # │ CLASS ATTRIBUTES
    # └─────────────────────────────────────────────────────────────────────────────────

    # Declare type of Class
    _Class: type[PyObInstance] | None

    # Declare type of counts
    _counts: dict[PyObInstance, Literal[1]]

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ __INIT__
    # └─────────────────────────────────────────────────────────────────────────────────

    def __init__(self) -> None:
        """Init Method"""

        # Initialize Class to None
        self._Class = None

        # Set counts attribute
        self._counts = {}

        # Set length attribute
        self._length = 0

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ STORE
    # └─────────────────────────────────────────────────────────────────────────────────

    def store(self, item: PyObInstance) -> PyObStore[PyObInstance]:
        """Adds a PyOb instance to the PyOb store"""

        # Check if Class is None
        if self._Class is None:

            # Check if item is not a PyObInstance
            if not is_pyob_instance(item):

                # Raise InvalidTypeError
                raise InvalidTypeError(
                    "Only PyOb instances can be added to a PyOb store",
                    received=item.__class__,
                )

            # Set class according to PyOb instance
            self._Class = item.__class__

        # Otherwise handle case of existing Class
        else:

            # Check if class of item does not match existing class
            # As PyOb stores should only allow instances of the same PyOb class
            if item.__class__ is not self._Class:

                # Raise UnexpectedTypeError
                raise UnexpectedTypeError(
                    "A PyOb store can only contain instances of the same PyOb class",
                    expected=self._Class,
                    received=item.__class__,
                )

        # Determine if length should be incremented
        # i.e. PyOb instance was not already stored
        should_increment = item not in self._counts

        # Add PyOb instance to counts
        self._counts[item] = 1

        # Check if length should be incremented
        # i.e. PyOb instance was actually added to counts
        if should_increment:

            # Increment length
            self._length += 1

        # Return PyOb store
        return self

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ UNSTORE
    # └─────────────────────────────────────────────────────────────────────────────────

    def unstore(self, item: PyObInstance) -> PyObStore[PyObInstance]:
        """Removes a PyOb instance from the PyOb store"""

        # Determine if length should be decremented
        # i.e. PyOb instance was already stored
        should_decrement = item in self._counts

        # Pop PyOb instance from counts
        self._counts.pop(item, None)

        # Check if length should be decremented
        # i.e. PyOb instance was actually removed from store
        if should_decrement:

            # Decrement length
            self._length -= 1

        # Return PyOb store
        return self
