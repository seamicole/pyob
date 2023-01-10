# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ PROJECT IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from pyob.main.classes.pyob import PyOb
from pyob.utils.functions.checkers import is_pyob_instance


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ TEST IS PYOB INSTANCE ACCEPTS PYOB SUBCLASS INSTANCES
# └─────────────────────────────────────────────────────────────────────────────────────


def test_is_pyob_instance_accepts_pyob_subclass_instances() -> None:
    """Tests that is_pyob_instance returns True for PyOb subclass instances"""

    # Define a parent PyOb class
    class ParentOne(PyOb):
        """A dummy parent PyOb class"""

    # Define a child PyOb class
    class ChildOne(ParentOne):
        """A dummy child PyOb class"""

    # Initialize dummy instances
    p1 = ParentOne()
    c1 = ChildOne()

    # Assert that parent instance is a PyOb instance
    assert is_pyob_instance(p1) is True

    # Assert that child instance is a PyOb instance
    assert is_pyob_instance(c1) is True


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ TEST IS PYOB INSTANCE REJECTS NON-PYOB SUBCLASS INSTANCES
# └─────────────────────────────────────────────────────────────────────────────────────


def test_is_pyob_instance_rejects_non_pyob_subclass_instances() -> None:
    """Tests that is_pyob_instance returns True for PyOb subclass instances"""

    # Define a dummy class
    class DummyClass:
        """A dummy non-PyOb class"""

    # Initialize dummy instances
    d1 = DummyClass()

    # Assert that dummy instance is not a PyOb instance
    assert is_pyob_instance(d1) is False
