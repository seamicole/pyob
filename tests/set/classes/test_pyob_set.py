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

        # Define a dummy PyOb class
        class DummyClass(PyOb):
            """A dummy PyOb class"""

        # Initialize dummy instances
        d1, d2, d3 = (DummyClass(), DummyClass(), DummyClass())

        # Define counts
        _counts = {d1: 1, d2: 2, d3: 3}

        # Initialize dummy set
        dummy_set = PyObSet[DummyClass](_counts=_counts)

        # Assert that dummy set is an instance of PyObs
        assert isinstance(dummy_set, PyObs)

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ TEST INIT FREZES COUNTS
    # └─────────────────────────────────────────────────────────────────────────────────

    def test_init_freezes_counts(self) -> None:
        """Tests that init method casts counts attribute to a FrozenDict"""

        # Define a dummy PyOb class
        class DummyClass(PyOb):
            """A dummy PyOb class"""

        # Initialize dummy instances
        d1, d2, d3 = (DummyClass(), DummyClass(), DummyClass())

        # Define counts
        _counts = {d1: 1, d2: 2, d3: 3}

        # Initialize dummy set
        dummy_set = PyObSet[DummyClass](_counts=_counts)

        # Assert that dummy set counts is a FrozenDict
        assert type(dummy_set._counts) is FrozenDict

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ TEST INIT REMOVES ZERO COUNTS
    # └─────────────────────────────────────────────────────────────────────────────────

    def test_init_removes_zero_counts(self) -> None:
        """Tests that init method removes PyObs with a count of zero"""

        # Define a dummy PyOb class
        class DummyClass(PyOb):
            """A dummy PyOb class"""

        # Initialize dummy instances
        d1, d2, d3, d4 = (DummyClass(), DummyClass(), DummyClass(), DummyClass())

        # Define counts
        _counts = {d1: 1, d2: 0, d3: 3, d4: -6}

        # Initialize dummy set
        dummy_set = PyObSet[DummyClass](_counts=_counts)

        # Assert that PyObs with a count of zero or less have been removed
        assert dummy_set._counts == {
            pyob: count for pyob, count in _counts.items() if count > 0
        }

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ TEST LENGTH METHODS RETURN SUM OF COUNTS
    # └─────────────────────────────────────────────────────────────────────────────────

    def test_length_methods_return_sum_of_counts(self) -> None:
        """Tests that all length methods return the sum of PyObs._counts"""

        # Define a dummy PyOb class
        class DummyClass(PyOb):
            """A dummy PyOb class"""

        # Initialize dummy instances
        d1, d2, d3 = (DummyClass(), DummyClass(), DummyClass())

        # Define counts
        _counts = {d1: 1, d2: 2, d3: 3}

        # Initialize dummy PyOb set
        dummy_set = PyObSet[DummyClass](_counts=_counts)

        # Get dummy set length
        dummy_set_length = sum(_counts.values())

        # Assert that the length dunder returns the correct value
        assert dummy_set.__len__() == len(dummy_set) == dummy_set_length

        # Assert that the length property returns the correct value
        assert dummy_set.length == dummy_set_length

        # Assert that the count method returns the correct value
        assert dummy_set.count() == dummy_set_length
