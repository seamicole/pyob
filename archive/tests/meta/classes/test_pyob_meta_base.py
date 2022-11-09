# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ PROJECT IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from pyob.meta.classes.pyob_meta_base import PyObMetaBase


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ TEST PYOB META BASE
# └─────────────────────────────────────────────────────────────────────────────────────


class TestPyObMetaBase:
    """A test class for PyObMetaBase"""

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ TEST DEFAULT ATTRIBUTES
    # └─────────────────────────────────────────────────────────────────────────────────

    def test_default_attributes(self):
        """Tests that PyObMetaBase contains all of the expected default attributes"""

        # Define default attributes
        default_attributes = {
            "Parents": None,
            "Children": None,
            "keys": None,
            "string": None,
            "label_singular": None,
            "label_plural": None,
        }

        # Define exceptions
        exceptions = {"__dict__", "__doc__", "__module__", "__weakref__"}

        # Iterate over attributes in PyObMetaBase
        for attribute in PyObMetaBase.__dict__:

            # Continue if attribute is an exception
            # Like default Python attributes like '__module__'
            if attribute in exceptions:
                continue

            # Assert that the attribute is defined in default attributes
            assert attribute in default_attributes

            # Assert that the attribute is initialized to the expected default value
            assert PyObMetaBase.__dict__[attribute] == default_attributes[attribute]

            # This assures us that we explicitly test any defaults we add in the future
            # i.e. we cannot easily change the PyObMetaBase attributes without testing
