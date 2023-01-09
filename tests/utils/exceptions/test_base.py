# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ PROJECT IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from pyob.utils.exceptions.base import Error


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ TEST ERROR
# └─────────────────────────────────────────────────────────────────────────────────────


class TestError:
    """A test class for pyob.utils.exceptions.base.Error"""

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ TEST INIT SETS MESSAGE
    # └─────────────────────────────────────────────────────────────────────────────────

    def test_init_sets_message(self) -> None:
        """Tests that the init method sets the message attribute"""

        # Define message
        message = "An unkown error occurred"

        # Initialize error instance
        error = Error(message)

        # Assert that message attribute is correct
        assert error.message == message

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ TEST STR COMBINES HEADLINE AND MESSAGE
    # └─────────────────────────────────────────────────────────────────────────────────

    def test_str_combines_headline_and_message(self) -> None:
        """Tests that the string method combines the error headline and message"""

        # Initialize error instance
        error = Error()

        # Get error string
        error_string = str(error)

        # Assert that error string is correct
        assert error_string == "\n\n" + error.headline + "\n"

        # Define non-empty message
        message = "An unknown error occurred"

        # Initialize error instance
        error = Error(message)

        # Get error string
        error_string = str(error)

        # Assert that error string is correct
        assert error_string == "\n\n" + error.headline + ": " + error.message + "\n"
