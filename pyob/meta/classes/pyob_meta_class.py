# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ GENERAL IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from __future__ import annotations

from typing import Generic, Sequence, TYPE_CHECKING, TypeVar

# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ PROJECT IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from pyob.store.classes.pyob_store import PyObStore
from pyob.utils.functions.sequence import freezeset

if TYPE_CHECKING:
    from pyob.types import Args, Kwargs, PyOb, PyObClass


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ PYOB META CLASS
# └─────────────────────────────────────────────────────────────────────────────────────

# Define a PyObClass TypeVar
PyObClassVar = TypeVar("PyObClassVar", bound="PyOb")


class PyObMetaClass(Generic[PyObClassVar]):
    """The root (pseudo-)metaclass for user-defined PyObMeta classes"""

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ CLASS ATTRIBUTES: PARENTS AND CHILDREN
    # └─────────────────────────────────────────────────────────────────────────────────

    # Declare type of Parents
    Parents: tuple[PyObClass, ...]

    # Declare type of Children
    Children: tuple[PyObClass, ...]

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ CLASS ATTRIBUTES: STORE
    # └─────────────────────────────────────────────────────────────────────────────────

    # Declare type of store instance
    store: PyObStore[PyObClassVar]

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ CLASS ATTRIBUTES: FIELD SETS
    # └─────────────────────────────────────────────────────────────────────────────────

    # Declare type of key fields
    keys: frozenset[str | frozenset[str]]

    # Declare type of unique fields
    uniques: frozenset[str | frozenset[str]]

    # Declare type of indexed fields
    indexes: frozenset[str | frozenset[str]]

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ __INIT__
    # └─────────────────────────────────────────────────────────────────────────────────

    def __init__(
        self,
        *args: Args,
        keys: Sequence[str | Sequence[str]] | None = None,
        uniques: Sequence[str | Sequence[str]] | None = None,
        indexes: Sequence[str | Sequence[str]] | None = None,
        **kwargs: Kwargs,
    ):
        """Init Method"""

        # ┌─────────────────────────────────────────────────────────────────────────────
        # │ PARENTS AND CHILDREN
        # └─────────────────────────────────────────────────────────────────────────────

        # Initialize tuple of parent classes
        # i.e. The subset of bases that are also PyOb classes
        self.Parents = ()

        # Initialize tuple of child classes
        # i.e. Any PyOb classes that end up inheriting from the current class
        self.Children = ()

        # ┌─────────────────────────────────────────────────────────────────────────────
        # │ STORE
        # └─────────────────────────────────────────────────────────────────────────────

        # Initialize PyObStore instance from store class
        self.store = PyObStore()

        # ┌─────────────────────────────────────────────────────────────────────────────
        # │ FIELD SETS
        # └─────────────────────────────────────────────────────────────────────────────

        # Initialize frozenset of key fields
        # i.e. A unique value across all fields
        # Value points to one instance
        self.keys = freezeset(keys or [])

        # Initialize frozenset of unique fields
        # i.e. A unique value for a given field
        # Value points to one instance given a field
        self.uniques = self.keys | freezeset(uniques or [])  # Keys unique by definition

        # Initialize frozenset of index fields
        # i.e. A non-unique value for a given field
        # Value points to many instances given a field
        self.indexes = freezeset(indexes or [])
