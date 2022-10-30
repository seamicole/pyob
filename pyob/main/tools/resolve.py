# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ GENERAL IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from typing import Optional, TYPE_CHECKING

# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ PROJECT IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

if TYPE_CHECKING:

    import pyob.main.classes.pyob


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ RESOLVE STRING FIELD
# └─────────────────────────────────────────────────────────────────────────────────────


def resolve_string_field(pyob: "pyob.main.classes.pyob.PyOb") -> Optional[str]:
    """Resolves and returns the best applicable string field for a PyOb instance"""

    # Initialize string field as PyObMeta.string
    # i.e. The field explicitly defined by the user
    string_field = pyob.PyObMeta.string

    # Default string field to the first available key if null
    # Provides a meaningful and unique string value for each PyOb
    string_field = string_field or (
        pyob.PyObMeta.keys[0] if pyob.PyObMeta.keys else None
    )

    # Return the string field
    return string_field
