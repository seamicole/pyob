# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ PROJECT IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from pyob.main.classes.pyob import PyOb
from pyob.utils.mixins.pyobs import PyObsMixin


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ TEST PYOBS MIXIN
# └─────────────────────────────────────────────────────────────────────────────────────


class TestPyObsMixin:
    """A test class for pyob.utils.mixins.pyobs_mixin.PyObsMixin"""

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ TEST LENGTH METHODS RETURN SUM OF COUNTS
    # └─────────────────────────────────────────────────────────────────────────────────

    def test_length_methods_return_sum_of_counts(self) -> None:
        """Tests that all length methods return the sum of PyObsMixin._counts"""

        # Define a dummy PyObClass
        class DummyClass(PyOb):
            """A dummy PyObClass"""

        # Initialize dummy instances
        d1, d2, d3 = (DummyClass(), DummyClass(), DummyClass())

        # Define counts
        _counts = {d1: 1, d2: 2, d3: 3}

        # Initialize dummy PyObs
        dummies = PyObsMixin(_counts=_counts)

        # Get dummy set length
        dummies_length = sum(_counts.values())

        # Assert that the length dunder returns the correct value
        assert dummies.__len__() == len(dummies) == dummies_length

        # Assert that the length property returns the correct value
        assert dummies.length == dummies_length

        # Assert that the count method returns the correct value
        assert dummies.count() == dummies_length
