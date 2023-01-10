# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ GENERAL IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from __future__ import annotations

from typing import TYPE_CHECKING

# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ PROJECT IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

if TYPE_CHECKING:
    from pyob.types import PyOb


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ STORE PYOB
# └─────────────────────────────────────────────────────────────────────────────────────


def store_pyob(pyob: PyOb) -> PyOb:
    """Adds a PyOb instance to the PyOb store"""

    # Add PyOb instance to PyOb store
    pyob.__class__._PyObMeta.store.store(pyob)

    # Return PyOb instance
    return pyob


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ UNSTORE PYOB
# └─────────────────────────────────────────────────────────────────────────────────────


def unstore_pyob(pyob: PyOb) -> PyOb:
    """Removes a PyOb instance from the PyOb store"""

    # Remove PyOb instance from PyOb store
    pyob.__class__._PyObMeta.store.unstore(pyob)

    # Return PyOb instance
    return pyob
