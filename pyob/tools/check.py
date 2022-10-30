# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ PROJECT IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

import pyob.main.classes.pyob as pyob  # Protects against circular imports


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ IS PYOB INSTANCE
# └─────────────────────────────────────────────────────────────────────────────────────


def is_pyob_instance(item) -> bool:
    """Returns a boolean of whether an item is a PyOb instance"""

    # Return boolean of whether item is a PyOb instance
    return isinstance(item, pyob.PyOb)
