# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ GENERAL IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from __future__ import annotations

from typing import Any

# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ PROJECT IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from pyob.main.classes import pyob


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ IS PYOB INSTANCE
# └─────────────────────────────────────────────────────────────────────────────────────


def is_pyob_instance(item: Any) -> bool:
    """Returns a boolean of whether an item is a PyOb instance"""

    # Return whether item is a PyOb instance
    return isinstance(item, pyob.PyOb)
