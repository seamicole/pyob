# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ GENERAL IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from __future__ import annotations
from typing import TYPE_CHECKING

# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ PROJECT IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

if TYPE_CHECKING:
    from pyob.types import Args, Kwargs, PyObChildren, PyObParents


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ PYOB META CLASS
# └─────────────────────────────────────────────────────────────────────────────────────


class PyObMetaClass:
    """The root (pseudo-)metaclass for user-defined PyObMeta classes"""

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ TYPE DECLARATION: PARENTS AND CHILDREN
    # └─────────────────────────────────────────────────────────────────────────────────

    # Declare type of Parents
    Parents: PyObParents

    # Declare type of Children
    Children: PyObChildren

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ __INIT__
    # └─────────────────────────────────────────────────────────────────────────────────

    def __init__(self, *args: Args, **kwargs: Kwargs):
        """Init Method"""

        # Initialize list of parent classes
        # i.e. The subset of bases that are also PyObClasses
        self.Parents = []

        # Initialize list of child classes
        # i.e. Any PyObClasses that end up inheriting from the current class
        self.Children = []
