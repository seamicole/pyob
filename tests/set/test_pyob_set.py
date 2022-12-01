# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ PROJECT IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from pyob.main.classes.pyob import PyOb
from pyob.set.classes.pyob_set import PyObSet


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ TEST PYOB SET
# └─────────────────────────────────────────────────────────────────────────────────────


class TestPyObSet:
    """A test class for pyob.set.classes.pyob_set.PyObSet"""

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ TEST LENGTH METHODS RETURN SUM OF COUNTS
    # └─────────────────────────────────────────────────────────────────────────────────

    def test_length_methods_return_sum_of_counts(self) -> None:
        """Tests that all length methods return the sum of PyObSet._counts"""

        # Define a dummy PyObClass
        class DummyClass(PyOb):
            """A dummy PyObClass"""

        # Initialize dummy instances
        d1, d2, d3 = (DummyClass(), DummyClass(), DummyClass())

        # Define counts
        _counts = {d1: 1, d2: 2, d3: 3}

        # Initialize dummy set
        dummy_set = PyObSet(_counts=_counts)

        # Get dummy set length
        dummy_set_length = sum(_counts.values())

        # Assert that the length dunder returns the correct value
        assert dummy_set.__len__() == len(dummy_set) == dummy_set_length

        # Assert that the length property returns the correct value
        assert dummy_set.length == dummy_set_length

        # Assert that the count method returns the correct value
        assert dummy_set.count() == dummy_set_length
