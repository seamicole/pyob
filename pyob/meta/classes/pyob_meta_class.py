# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ GENERAL IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from __future__ import annotations
from typing import Sequence, TYPE_CHECKING

# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ PROJECT IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

if TYPE_CHECKING:
    from pyob.types import Args, Kwargs, PyObClass


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ PYOB META CLASS
# └─────────────────────────────────────────────────────────────────────────────────────


class PyObMetaClass:
    """The root (pseudo-)metaclass for user-defined PyObMeta classes"""

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ TYPE DECLARATION: PARENTS AND CHILDREN
    # └─────────────────────────────────────────────────────────────────────────────────

    # Declare type of Parents
    Parents: list[PyObClass]

    # Declare type of Children
    Children: list[PyObClass]

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ TYPE DECLARATION: LOOKUP FIELDS
    # └─────────────────────────────────────────────────────────────────────────────────

    # Declare type of unique fields
    unique: frozenset[str]

    # Declare type of indexed fields
    indexes: frozenset[str]

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ __INIT__
    # └─────────────────────────────────────────────────────────────────────────────────

    def __init__(
        self,
        *args: Args,
        unique: Sequence[str] | None = None,
        indexes: Sequence[str] | None = None,
        **kwargs: Kwargs,
    ):
        """Init Method"""

        # Initialize list of parent classes
        # i.e. The subset of bases that are also PyObClasses
        self.Parents = []

        # Initialize list of child classes
        # i.e. Any PyObClasses that end up inheriting from the current class
        self.Children = []
