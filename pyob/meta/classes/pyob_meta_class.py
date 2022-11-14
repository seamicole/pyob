# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ GENERAL IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from __future__ import annotations

from typing import Sequence, TYPE_CHECKING

# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ PROJECT IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from pyob.tools.sequence import freezeset

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
    # │ TYPE DECLARATION: CONSTRAINTS
    # └─────────────────────────────────────────────────────────────────────────────────

    # Declare type of indexed fields
    indexes: frozenset[str | frozenset[str]]

    # Declare type of unique fields
    uniques: frozenset[str | frozenset[str]]

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ __INIT__
    # └─────────────────────────────────────────────────────────────────────────────────

    def __init__(
        self,
        *args: Args,
        uniques: Sequence[str | Sequence[str]] | None = None,
        indexes: Sequence[str | Sequence[str]] | None = None,
        **kwargs: Kwargs,
    ):
        """Init Method"""

        # ┌─────────────────────────────────────────────────────────────────────────────
        # │ PARENTS AND CHILDREN
        # └─────────────────────────────────────────────────────────────────────────────

        # Initialize list of parent classes
        # i.e. The subset of bases that are also PyObClasses
        self.Parents = []

        # Initialize list of child classes
        # i.e. Any PyObClasses that end up inheriting from the current class
        self.Children = []

        # ┌─────────────────────────────────────────────────────────────────────────────
        # │ CONSTRAINTS
        # └─────────────────────────────────────────────────────────────────────────────

        # Initialize frozenset of index fields
        self.indexes = freezeset(indexes or [])

        # Initialize frozenset of unique fields
        self.uniques = freezeset(uniques or [])
