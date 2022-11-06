# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ GENERAL IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from beartype.door import is_bearable

# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ PROJECT IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

import pyob.main.classes.pyob as pyob  # Protects against circular imports
import pyob.store.classes.pyob_store as pyob_store  # Protects against circular imports

from pyob.exceptions import InvalidTypeError
from pyob.types import Sequence


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ IS PYOB INSTANCE
# └─────────────────────────────────────────────────────────────────────────────────────


def is_pyob_instance(item, **kwargs) -> bool:
    """Returns a boolean of whether an item is a PyOb instance"""

    # Return boolean of whether item is a PyOb instance
    return is_type(item, pyob.PyOb, **kwargs)


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ IS PYOB STORE INSTANCE
# └─────────────────────────────────────────────────────────────────────────────────────


def is_pyob_store_instance(item, **kwargs) -> bool:
    """Returns a boolean of whether an item is a PyObStore instance"""

    # Return boolean of whether item is a PyObStore instance
    return is_type(item, pyob_store.PyObStore, **kwargs)


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ IS SEQUENCE
# └─────────────────────────────────────────────────────────────────────────────────────


def is_sequence(item, **kwargs):
    """Returns a boolean of whether an item is a sequence"""

    # Return boolean of whether item is a sequence
    return is_type(item, Sequence, **kwargs)


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ IS TYPE
# └─────────────────────────────────────────────────────────────────────────────────────


def is_type(
    item, annotation, raise_if: bool | None = None, message: str | None = None
) -> bool:
    """Returns a boolean of whether an item conforms to a type annotation"""

    # Determine if item conforms to annotation
    _is_type = is_bearable(item, annotation)

    # Determine if should raise
    should_raise = (_is_type is True and raise_if is True) or (
        _is_type is False and raise_if is False
    )

    # Check if should raise an InvalidTypeError
    if should_raise:

        # Define annotation key
        annotation_key = "Unwanted" if raise_if is True else "Expected"

        # Add quotations if item is string
        item = f"'{item}'" if type(item) is str else item

        # Construct message
        message = (
            "Invalid type encountered!"
            f"\n\n{annotation_key}: {annotation}"
            f"\nReceived: {type(item)}"
            f"\nVariable: {item}" + (("\n\n" + message) if message else "")
        )

        # Raise InvalidTypeError
        raise InvalidTypeError(message)

    # Return boolean of whether item conforms to annotation
    return _is_type
