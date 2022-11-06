# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ GENERAL IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from typing import TYPE_CHECKING

# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ PROJECT IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from pyob.main.tools.resolve import resolve_string_field
from pyob.tools.check import is_pyob_instance
from pyob.tools.object import hexify
from pyob.tools.string import pascalize

if TYPE_CHECKING:
    import pyob.main.classes.pyob.PyOb


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ PYOB DUNDER MIXIN
# └─────────────────────────────────────────────────────────────────────────────────────


class PyObDunderMixin:
    """A mixin for PyOb dunder methods"""

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ __REPR__
    # └─────────────────────────────────────────────────────────────────────────────────

    def __repr__(self) -> str:
        """Representation Dunder Method"""

        # Initialize representation to singular label
        representation = self.PyObMeta.label_singular

        # Convert representation to Pascal case
        representation = pascalize(representation)

        # Add angle brackets to representation
        representation = f"<{representation}: {str(self)}>"

        # Return representation
        return representation

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ __STR__
    # └─────────────────────────────────────────────────────────────────────────────────

    def __str__(self, root: "pyob.main.classes.pyob.PyOb" | None = None) -> str:
        """String Dunder Method"""

        # Initialize root PyOb instance
        # Used to avoid cases of infinite recursion
        # since string field values may be other PyOb instances
        root = root if root is not None else self

        # Resolve the string field of the PyOb instance
        string_field = resolve_string_field(self)

        # Get string value from string field
        string_value = string_field and getattr(self, string_field, None)

        # Check if the string value is another PyOb instance
        # Analagous to the field of of a PyOb instance being a "foreign key" to another
        if is_pyob_instance(string_value):

            # Check if the associated PyOb instance isn't root and has a string field
            # If is the root then we are likely going around in circles and must break
            # If the associate PyOb instance doesn't have a string field, ignore it
            if string_value != root and resolve_string_field(string_value):

                # Evaluate the string value of the associated PyOb instance
                # We pass the root here for tracking to avoid infinite recursion
                string_value = string_value.__str__(root=root)

            # Otherwise handle case of no meaningful string value
            else:

                # Set string value to None
                # We avoid setting string value to hex of an associated PyOb instance
                # as this would be incredibly confusing
                string_value = None

        # Ensure that the string value defaults to the hex of the root if null
        string_value = string_value or hexify(root)

        # Ensure that the string value is a string
        string_value = str(string_value)

        # Return the string value
        return string_value
