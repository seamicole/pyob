# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ GENERAL IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from unittest.mock import patch

# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ PROJECT IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from pyob.utils.exceptions.base import Error
from pyob.utils.exceptions.validation import InvalidTypeError


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ TEST INVALID TYPE ERROR
# └─────────────────────────────────────────────────────────────────────────────────────


class TestInvalidTypeError:
    """A test class for pyob.utils.exceptions.validation.InvalidTypeError"""

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ TEST INIT CALLS ERROR INIT METHOD
    # └─────────────────────────────────────────────────────────────────────────────────

    def test_init_calls_error_init_method(self) -> None:
        """Tests that the init method calls Error.__init__"""

        # Define message
        message = "An unkown error occurred"

        # Initialize mock patch block
        with patch.object(Error, "__init__") as mock:

            # Initialize InvalidTypeError instance
            InvalidTypeError(message=message)

        # Assert that PyObStore.store() was called
        mock.assert_called_once_with(message=message)

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ TEST INIT SETS EXPECTED AND RECEIVED
    # └─────────────────────────────────────────────────────────────────────────────────

    def test_init_sets_expected_and_recevied(self) -> None:
        """Tests that the init method sets the expected and received attributes"""

        # Define dummy class
        class DummyClassOne:
            """A dummy class"""

        # Define dummy class
        class DummyClassTwo:
            """A dummy class"""

        # Initialize InvalidTypeError instance
        error = InvalidTypeError(expected=DummyClassOne, received=DummyClassTwo)

        # Assert that expected attribute is correct
        assert error.expected is DummyClassOne

        # Assert that received attribute is correct
        assert error.received is DummyClassTwo

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ TEST STR CALLS ERROR STR METHOD
    # └─────────────────────────────────────────────────────────────────────────────────

    def test_str_calls_error_str_method(self) -> None:
        """Tests that the string method calls Error.__str__"""

        # Initialize mock patch block
        with patch.object(Error, "__str__") as mock:

            # Initialize InvalidTypeError instance
            error = InvalidTypeError()

            # Construct error string
            error.__str__()

        # Assert that PyObStore.store() was called
        mock.assert_called_once()

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ TEST STR CONCATENATES EXPECTED AND RECEIVED TO ERROR STRING
    # └─────────────────────────────────────────────────────────────────────────────────

    def test_str_concatenates_expected_and_received_to_error_string(self) -> None:
        """Tests that the string method combines the error headline and message"""

        # Define non-empty message
        message = "An unknown error occurred"

        # Define dummy class
        class DummyClassOne:
            """A dummy class"""

        # Define dummy class
        class DummyClassTwo:
            """A dummy class"""

        # Initialize error instance
        error = InvalidTypeError(message=message, expected=DummyClassOne)

        # Get error string
        error_string = str(error)

        # Assert that error string is correct
        assert (
            error_string
            == "\n\n"
            + error.headline
            + ": "
            + message
            + "\n\n"
            + "Expected: "
            + str(DummyClassOne)
            + "\n\n"
        )

        # Initialize error instance
        error = InvalidTypeError(message=message, received=DummyClassTwo)

        # Get error string
        error_string = str(error)

        # Assert that error string is correct
        assert (
            error_string
            == "\n\n"
            + error.headline
            + ": "
            + message
            + "\n\n"
            + "Received: "
            + str(DummyClassTwo)
            + "\n\n"
        )

        # Initialize error instance
        error = InvalidTypeError(
            message=message, expected=DummyClassOne, received=DummyClassTwo
        )

        # Get error string
        error_string = str(error)

        # Assert that error string is correct
        assert (
            error_string
            == "\n\n"
            + error.headline
            + ": "
            + message
            + "\n\n"
            + "Expected: "
            + str(DummyClassOne)
            + "\n"
            + "Received: "
            + str(DummyClassTwo)
            + "\n\n"
        )
