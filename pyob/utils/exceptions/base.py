# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ ERROR
# └─────────────────────────────────────────────────────────────────────────────────────


class Error(Exception):
    """An abstract error base class"""

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ CLASS ATTRIBUTES
    # └─────────────────────────────────────────────────────────────────────────────────

    # Declare type and value of headline
    headline: str = "Error Encountered"

    # Declare type of message
    message: str

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ __INIT__
    # └─────────────────────────────────────────────────────────────────────────────────

    def __init__(self, message: str = "") -> None:
        """Init Method"""

        # Call parent init method
        super().__init__(message)

        # Set message
        self.message = message

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ __STR__
    # └─────────────────────────────────────────────────────────────────────────────────

    def __str__(self) -> str:
        """String Method"""

        # Initialize string
        string = "\n\n" + self.headline

        # Get message
        message = self.message

        # Check if message is not null
        if message:

            # Add message to string
            string += ": " + message

        # Add a new line to the string
        string += "\n"

        # Return string
        return string
