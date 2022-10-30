# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ PROJECT IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from pyob import PyOb
from pyob.tools.check import is_pyob_instance


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
        """A non-PyOb class"""

    # Initialize a non-PyOb instance
    non_pyob = NonPyObClass()

    # Assert that non-PyOb instance returns False
    assert is_pyob_instance(non_pyob) is False
