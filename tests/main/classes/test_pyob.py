# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ GENERAL IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from unittest.mock import patch

# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ PROJECT IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from pyob.main.classes.pyob import PyOb


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ TEST PYOB
# └─────────────────────────────────────────────────────────────────────────────────────


class TestPyOb:
    """A test class for pyob.main.classes.pyob.PyOb"""

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ TEST NEG CALLS UNSTORE PYOB
    # └─────────────────────────────────────────────────────────────────────────────────

    def test_neg_calls_unstore_pyob(self) -> None:
        """Tests that PyOb.__neg__ calls unstore_pyob"""

        # Define a dummy PyOb class
        class DummyClass(PyOb):
            """A dummy PyOb class"""

        # Initialize dummy instance
        d1 = DummyClass()

        # Initialize mock patch block
        with patch("pyob.main.classes.pyob.unstore_pyob") as mock:

            # Call __neg__ method
            d1.__neg__()

        # Assert that unstore_pyob was called
        mock.assert_called_once_with(d1)

        # Initialize mock patch block
        with patch("pyob.main.classes.pyob.unstore_pyob") as mock:

            # Invoke __neg__ operator
            -d1

        # Assert that unstore_pyob was called
        mock.assert_called_once_with(d1)

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ TEST POS CALLS STORE PYOB
    # └─────────────────────────────────────────────────────────────────────────────────

    def test_pos_calls_store_pyob(self) -> None:
        """Tests that PyOb.__pos__ calls store_pyob"""

        # Define a dummy PyOb class
        class DummyClass(PyOb):
            """A dummy PyOb class"""

        # Initialize dummy instance
        d1 = DummyClass()

        # Initialize mock patch block
        with patch("pyob.main.classes.pyob.store_pyob") as mock:

            # Call __pos__ method
            d1.__pos__()

        # Assert that store_pyob was called
        mock.assert_called_once_with(d1)

        # Initialize mock patch block
        with patch("pyob.main.classes.pyob.store_pyob") as mock:

            # Invoke __pos__ operator
            +d1

        # Assert that store_pyob was called
        mock.assert_called_once_with(d1)

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ TEST STORE CALLS STORE PYOB
    # └─────────────────────────────────────────────────────────────────────────────────

    def test_store_calls_store_pyob(self) -> None:
        """Tests that PyOb.store calls store_pyob"""

        # Define a dummy PyOb class
        class DummyClass(PyOb):
            """A dummy PyOb class"""

        # Initialize dummy instance
        d1 = DummyClass()

        # Initialize mock patch block
        with patch("pyob.main.classes.pyob.store_pyob") as mock:

            # Call store method
            d1.store()

        # Assert that store_pyob was called
        mock.assert_called_once_with(d1)

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ TEST UNSTORE CALLS UNSTORE PYOB
    # └─────────────────────────────────────────────────────────────────────────────────

    def test_unstore_calls_unstore_pyob(self) -> None:
        """Tests that PyOb.unstore calls unstore_pyob"""

        # Define a dummy PyOb class
        class DummyClass(PyOb):
            """A dummy PyOb class"""

        # Initialize dummy instance
        d1 = DummyClass()

        # Initialize mock patch block
        with patch("pyob.main.classes.pyob.unstore_pyob") as mock:

            # Call unstore method
            d1.unstore()

        # Assert that unstore_pyob was called
        mock.assert_called_once_with(d1)
