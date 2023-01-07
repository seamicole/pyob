# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ GENERAL IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from unittest.mock import patch

# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ PROJECT IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from pyob.main.classes.pyob import PyOb
from pyob.main.functions.store import store_pyob, unstore_pyob


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ TEST STORE PYOB CALLS STORE METHOD
# └─────────────────────────────────────────────────────────────────────────────────────


def test_store_pyob_calls_store_method() -> None:
    """Tests that store_pyob calls PyObStore.store"""

    # Define a dummy PyOb class
    class DummyClass(PyOb):
        """A dummy PyOb class"""

    # Initialize dummy instance
    d1 = DummyClass()

    # Initialize mock patch block
    with patch.object(DummyClass._PyObMeta.store, "store") as mock:

        # Add dummy instance to store
        store_pyob(d1)

    # Assert that PyObStore.store() was called
    mock.assert_called_once_with(d1)


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ TEST UNSTORE PYOB CALLS UNSTORE METHOD
# └─────────────────────────────────────────────────────────────────────────────────────


def test_unstore_pyob_calls_unstore_method() -> None:
    """Tests that unstore_pyob calls PyObStore.unstore"""

    # Define a dummy PyOb class
    class DummyClass(PyOb):
        """A dummy PyOb class"""

    # Initialize dummy instance
    d1 = DummyClass()

    # Initialize mock patch block
    with patch.object(DummyClass._PyObMeta.store, "unstore") as mock:

        # Add dummy instance to store
        unstore_pyob(d1)

    # Assert that PyObStore.store() was called
    mock.assert_called_once_with(d1)
