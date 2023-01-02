# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ PROJECT IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from pyob.main.classes.pyob import PyOb
from pyob.set.classes.pyob_set import PyObSet
from pyob.utils.classes.sequence import FrozenDict
from pyob.utils.mixins.pyobs import PyObs


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ TEST PYOB SET
# └─────────────────────────────────────────────────────────────────────────────────────


class TestPyObSet:
    """A test class for pyob.set.classes.pyob_set.PyObSet"""

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ TEST PYOB SET SUBCLASSES PYOBS MIXIN
    # └─────────────────────────────────────────────────────────────────────────────────

    def test_pyob_set_subclasses_pyobs_mixin(self) -> None:
        """Tests that PyObSet is a subclass of PyObs"""

        # Assert that PyObSet is a subclass of PyObs
        assert issubclass(PyObSet, PyObs)

        # Define a dummy PyObClass
        class DummyClass(PyOb):
            """A dummy PyObClass"""

        # Initialize dummy instances
        d1, d2, d3 = (DummyClass(), DummyClass(), DummyClass())

        # Define counts
        _counts = {d1: 1, d2: 2, d3: 3}

        # Initialize dummy set
        dummy_set = PyObSet(_counts=_counts)

        # Assert that dummy set is an instance of PyObs
        assert isinstance(dummy_set, PyObs)

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ TEST PYOB SET FREZES COUNTS
    # └─────────────────────────────────────────────────────────────────────────────────

    def test_pyob_set_freezes_counts(self) -> None:
        """Tests that PyObSet instances cast counts attribute to a FrozenDict"""

        # Define a dummy PyObClass
        class DummyClass(PyOb):
            """A dummy PyObClass"""

        # Initialize dummy instances
        d1, d2, d3 = (DummyClass(), DummyClass(), DummyClass())

        # Define counts
        _counts = {d1: 1, d2: 2, d3: 3}

        # Initialize dummy set
        dummy_set = PyObSet(_counts=_counts)

        # Assert that dummy set counts is a FrozenDict
        assert type(dummy_set._counts) is FrozenDict
