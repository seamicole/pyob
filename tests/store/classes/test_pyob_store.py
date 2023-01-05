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
    # │ TEST PYOB STORE SUBCLASSES PYOBS
    # └─────────────────────────────────────────────────────────────────────────────────

    def test_pyob_store_subclasses_pyobs(self) -> None:
        """Tests that PyObStore is a subclass of PyObs"""

        # Assert that PyObSet is a subclass of PyObs
        assert issubclass(PyObStore, PyObs)

        # Define a dummy PyObClass
        class DummyClass(PyOb):
            """A dummy PyObClass"""

        # Initialize dummy store
        dummy_store = PyObStore[DummyClass]()

        # Assert that dummy store is an instance of PyObs
        assert isinstance(dummy_store, PyObs)

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ TEST LENGTH METHODS RETURN SUM OF COUNTS
    # └─────────────────────────────────────────────────────────────────────────────────

    def test_length_methods_return_sum_of_counts(self) -> None:
        """Tests that all length methods return the sum of PyObs._counts"""

        # Define a dummy PyOb class
        class DummyClass(PyOb):
            """A dummy PyObClass"""

        # Initialize dummy PyOb store
        dummy_store = PyObStore[DummyClass]()

        # Assert that the store counts is an empty dictionary
        assert dummy_store._counts == {}

        # Assert that the length dunder returns the correct value
        assert dummy_store.__len__() == len(dummy_store) == 0

        # Assert that the length property returns the correct value
        assert dummy_store.length == 0

        # Assert that the count method returns the correct value
        assert dummy_store.count() == 0

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ TEST STORE ADDS PYOB INSTANCE TO COUNTS
    # └─────────────────────────────────────────────────────────────────────────────────

    def test_store_adds_pyob_instance_to_counts(self) -> None:
        """Tests that store method adds a PyOb instance to counts dictionary"""

        # Define a dummy PyObClass
        class DummyClass(PyOb):
            """A dummy PyObClass"""

        # Get dummy store
        dummy_store = DummyClass._PyObMeta.store

        # Assert that the dummy store counts equals an empty dictionary
        assert dummy_store._counts == {}

        # Initialize dummy instances
        d1 = DummyClass()

        # Add instance to store
        dummy_store = dummy_store.store(d1)

        # Assert that the dummy store counts reflects the add operation
        assert dummy_store._counts == {d1: 1}

        # Try to add the same instance twice
        dummy_store = dummy_store.store(d1)

        # Assert that the dummy store counts haven't changed
        # Because the store is meant to store no more than one of every instance
        assert dummy_store._counts == {d1: 1}

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ TEST UNSTORE REMOVES PYOB INSTANCE FROM COUNTS
    # └─────────────────────────────────────────────────────────────────────────────────

    def test_unstore_removes_pyob_instance_from_counts(self) -> None:
        """Tests that unstore method removes a PyOb instance from counts dictionary"""

        # Define a dummy PyObClass
        class DummyClass(PyOb):
            """A dummy PyObClass"""

        # Get dummy store
        dummy_store = DummyClass._PyObMeta.store

        # Initialize dummy instances
        d1 = DummyClass()

        # Add dummy instances to dummy store
        dummy_store.store(d1)

        # Assert that the dummy store counts reflects the remove operation
        assert dummy_store._counts == {d1: 1}

        # Remove instance from store
        dummy_store = dummy_store.unstore(d1)

        # Assert that the dummy store counts reflects the remove operation
        assert dummy_store._counts == {}

        # Try to remove the same instance twice
        dummy_store = dummy_store.unstore(d1)

        # Assert that the dummy store counts haven't changed
        assert dummy_store._counts == {}
