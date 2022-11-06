# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ GENERAL IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

import pytest

# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ PROJECT IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from pyob import PyOb
from pyob.exceptions import InvalidTypeError
from pyob.tools.check import (
    is_pyob_instance,
    is_pyob_store_instance,
    is_sequence,
    is_type,
)


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ TEST IS PYOB INSTANCE
# └─────────────────────────────────────────────────────────────────────────────────────


def test_is_pyob_instance() -> None:
    """Tests the expected output of the pyob.tools.check.is_pyob_instance function"""

    # Define a PyOb class
    class PyObClass(PyOb):
        """A PyOb class"""

    # Initialize a PyOb instance
    pyob = PyObClass()

    # Assert that PyOb instance returns True
    assert is_pyob_instance(pyob) is True

    # Define a non-PyOb class
    class NonPyObClass:
        """A non-PyObClass"""

    # Initialize a non-PyOb instance
    non_pyob = NonPyObClass()

    # Assert that non-PyOb instance returns False
    assert is_pyob_instance(non_pyob) is False


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ TEST IS PYOB STORE INSTANCE
# └─────────────────────────────────────────────────────────────────────────────────────


def test_is_pyob_store_instance() -> None:
    """
    Tests the expected output of the pyob.tools.check.is_pyob_store_instance function
    """

    # Define a PyOb class
    class PyObClass(PyOb):
        """A PyOb class"""

    # Initialize a PyOb instance
    pyob = PyObClass()

    # Assert that PyObStore instance returns True
    assert is_pyob_store_instance(pyob.PyObMeta.store) is True

    # Assert that PyOb instance returns False
    assert is_pyob_store_instance(pyob) is False


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ TEST IS SEQUENCE
# └─────────────────────────────────────────────────────────────────────────────────────


def test_is_sequence() -> None:
    """Tests the expected output of the pyob.tools.check.is_sequence function"""

    # Define items
    items = (1, "one", True)

    # Assert that a list of items is a sequence
    assert is_sequence(list(items)) is True

    # Assert that a set of items is a sequence
    assert is_sequence(set(items)) is True

    # Assert that a tuple of items is a sequence
    assert is_sequence(tuple(items)) is True

    # Assert that a dictionary if items is not a sequence
    assert is_sequence({"one": 1, 1: True, "True": "one"}) is False


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ TEST IS TYPE
# └─────────────────────────────────────────────────────────────────────────────────────


def test_is_type() -> None:
    """Tests the expected output of the pyob.tools.check.is_type function"""

    # Assert that is type returns True when expected
    assert is_type(5, int) is True

    # Assert that is type returns False when expected
    assert is_type("five", int) is False

    # Assert that nothing is raised if raise condition not met
    assert is_type("five", int, raise_if=True) is False

    # Initialize raises block
    with pytest.raises(InvalidTypeError):

        # Raise an InvalidTypeError on non-matching type
        is_type("five", int, raise_if=False)

    # Raise an InvalidTypeError on matching type
    assert is_type("five", str, raise_if=False) is True

    # Initialize raises block
    with pytest.raises(InvalidTypeError):

        # Raise an InvalidTypeError on matching type
        is_type("five", str, raise_if=True)
