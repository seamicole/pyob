# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ GENERAL IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from __future__ import annotations

# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ PROJECT IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from pyob.main.functions.store import store_pyob, unstore_pyob
from pyob.meta.classes.pyob_class import PyObClass


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ PYOB
# └─────────────────────────────────────────────────────────────────────────────────────


class PyOb(metaclass=PyObClass):
    """An abstract root class for all user-defined PyOb classes"""

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ __NEG__
    # └─────────────────────────────────────────────────────────────────────────────────

    def __neg__(self) -> PyOb:
        """Negative Method"""

        # Unstore and return the PyOb instance
        return unstore_pyob(self)

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ __POS__
    # └─────────────────────────────────────────────────────────────────────────────────

    def __pos__(self) -> PyOb:
        """Positive Method"""

        # Store and return the PyOb instance
        return store_pyob(self)

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ STORE
    # └─────────────────────────────────────────────────────────────────────────────────

    def store(self) -> PyOb:
        """Stores a PyOb instance in the PyOb store"""

        # Store and return the PyOb instance
        return store_pyob(self)

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ UNSTORE
    # └─────────────────────────────────────────────────────────────────────────────────

    def unstore(self) -> PyOb:
        """Unstores a PyOb instance from the PyOb store"""

        # Unstore and return the PyOb instance
        return unstore_pyob(self)
