# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ PROJECT IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from pyob.tools.object import hexify


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ TEST HEXIFY
# └─────────────────────────────────────────────────────────────────────────────────────


def test_hexify() -> None:
    """Tests the expected output of the pyob.tools.object.hexify function"""

    # Define a dummy class
    class Dummy:
        """A dummy class"""

    # Initialize a dummy instance
    dummy = Dummy()

    # Assert the hexify returns the hex ID of the dummy instance
    assert hexify(dummy) == hex(id(dummy))
