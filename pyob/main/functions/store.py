# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ GENERAL IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from __future__ import annotations

from typing import TYPE_CHECKING

# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ PROJECT IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

if TYPE_CHECKING:
    from pyob.types import PyObInstance


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ STORE PYOB
# └─────────────────────────────────────────────────────────────────────────────────────


def store_pyob(pyob: PyObInstance) -> PyObInstance:
    """Adds a PyOb instance to the PyOb store"""

    # Add PyOb instance to PyOb store
    pyob.__class__._PyObMeta.store.add(pyob)

    # Return PyOb instance
    return pyob


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ UNSTORE PYOB
# └─────────────────────────────────────────────────────────────────────────────────────


def unstore_pyob(pyob: PyObInstance) -> PyObInstance:
    """Removes a PyOb instance from the PyOb store"""

    # Add PyOb instance to PyOb store
    pyob.__class__._PyObMeta.store.remove(pyob)

    # Return PyOb instance
    return pyob
