# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ PROJECT IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from pyob.main.classes.pyob import PyOb
from pyob.store.classes.pyob_store import PyObStore
from pyob.utils.mixins.pyobs import PyObs


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ TEST PYOB STORE
# └─────────────────────────────────────────────────────────────────────────────────────


class TestPyObStore:
    """A test class for pyob.set.classes.pyob_store.PyObStore"""

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ TEST PYOB STORE SUBCLASSES PYOBS MIXIN
    # └─────────────────────────────────────────────────────────────────────────────────

    def test_pyob_store_subclasses_pyobs_mixin(self) -> None:
        """Tests that PyObStore is a subclass of PyObs"""

        # Assert that PyObSet is a subclass of PyObs
        assert issubclass(PyObStore, PyObs)

        # Define a dummy PyObClass
        class DummyClass(PyOb):
            """A dummy PyObClass"""

        # Initialize dummy instances
        d1, d2, d3 = (DummyClass(), DummyClass(), DummyClass())

        # Define counts
        _counts = {d1: 1, d2: 1, d3: 1}

        # Initialize dummy store
        dummy_store = PyObStore(_counts=_counts)

        # Assert that dummy store is an instance of PyObs
        assert isinstance(dummy_store, PyObs)

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ TEST ADD INCREMENTS COUNT
    # └─────────────────────────────────────────────────────────────────────────────────

    def test_add_increments_count(self) -> None:
        """Tests that PyObStore add methods increment to count attribute as expected"""

        # Define a dummy PyObClass
        class DummyClass(PyOb):
            """A dummy PyObClass"""

        # Get dummy store
        dummy_store = DummyClass._PyObMeta.store

        # Assert that the dummy store counts equals an empty dictionary
        assert dummy_store._counts == {}

        # Initialize dummy instances
        d1 = DummyClass()
        d2 = DummyClass()

        # Add instance via __add__
        dummy_store = dummy_store + d1

        # Assert that the dummy store counts reflects the add operation
        assert dummy_store._counts == {d1: 1}

        # Try to add the same instance twice
        dummy_store = dummy_store + d1

        # Assert that the dummy store counts haven't changed
        # Because the store is meant to store no more than one of every instance
        assert dummy_store._counts == {d1: 1}

        # Add instance via add
        dummy_store = dummy_store.add(d2)

        # Assert that the dummy store counts reflects the add operation
        assert dummy_store._counts == {d1: 1, d2: 1}

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ TEST SUM DECREMENTS COUNT
    # └─────────────────────────────────────────────────────────────────────────────────

    def test_sub_decrements_count(self) -> None:
        """Tests that PyObStore sub methods decrement count attribute as expected"""

        # Define a dummy PyObClass
        class DummyClass(PyOb):
            """A dummy PyObClass"""

        # Get dummy store
        dummy_store = DummyClass._PyObMeta.store

        # Initialize dummy instances
        d1 = DummyClass()
        d2 = DummyClass()

        # Add dummy instances to dummy store
        dummy_store.add(d1)
        dummy_store.add(d2)

        # Assert that the dummy store counts reflects the sub operation
        assert dummy_store._counts == {d1: 1, d2: 1}

        # Remove instance via __sub__
        dummy_store = dummy_store - d1

        # Assert that the dummy store counts reflects the sub operation
        assert dummy_store._counts == {d2: 1}

        # Try to remove the same instance twice
        dummy_store = dummy_store - d1

        # Assert that the dummy store counts haven't changed
        assert dummy_store._counts == {d2: 1}

        # Add instance via remove
        dummy_store = dummy_store.remove(d2)

        # Assert that the dummy store counts reflects the sub operation
        assert dummy_store._counts == {}
