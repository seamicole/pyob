# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ GENERAL IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from __future__ import annotations
from typing import TYPE_CHECKING

# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ PROJECT IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from pyob.meta.classes.pyob_class import PyObClass

if TYPE_CHECKING:
    from pyob.types import AnyClass


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ IS PYOB CLASS
# └─────────────────────────────────────────────────────────────────────────────────────


def is_pyob_class(Class: AnyClass) -> bool:
    """Returns a boolean of whether an class is a PyOb subclass"""

    # Return a boolean of whether the class is a PyOb subclass
    return type(Class) is PyObClass
