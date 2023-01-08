# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ PROJECT IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from pyob.utils.exceptions.base import Error


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ INVALID TYPE ERROR
# └─────────────────────────────────────────────────────────────────────────────────────


class InvalidTypeError(Error):
    """Invalid Type Error"""

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ CLASS ATTRIBUTES
    # └─────────────────────────────────────────────────────────────────────────────────

    # Declare value of headline
    headline = "Invalid Type Encountered"

    # Declare type of message
    message: str

    # Declare type and value of expected
    expected: type | None = None

    # Declare type and value of received
    received: type | None = None

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ __INIT__
    # └─────────────────────────────────────────────────────────────────────────────────

    def __init__(
        self,
        message: str = "",
        expected: type | None = None,
        received: type | None = None,
    ) -> None:
        """Init Method"""

        # Call parent init method
        super().__init__(message=message)

        # Set expected and received
        self.expected = expected
        self.received = received

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ __STR__
    # └─────────────────────────────────────────────────────────────────────────────────

    def __str__(self) -> str:
        """String Method"""

        # Call parent string method
        string = super().__str__()

        # Initialize summary
        summary = ""

        # Iterate over expected and received classes
        for prefix, Class in (("expected", self.expected), ("received", self.received)):

            # Continue if None
            if Class is None:
                continue

            # Add to summary
            summary += prefix.title() + ": " + str(Class) + "\n"

        # Check if summary is not null
        if summary:

            # Add summary to string
            string += "\n" + summary + "\n"

        # Return string
        return string


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ UNEXPECTED TYPE ERROR
# └─────────────────────────────────────────────────────────────────────────────────────


class InvalidTypeError(InvalidTypeError):
    """Invalid Type Error"""

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ CLASS ATTRIBUTES
    # └─────────────────────────────────────────────────────────────────────────────────

    # Declare value of headline
    headline = "Unexpected Type Encountered"
