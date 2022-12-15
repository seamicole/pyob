# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ GENERAL IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from __future__ import annotations

from typing import TYPE_CHECKING, Any

# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ PROJECT IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from pyob.meta.classes.pyob_meta_class import PyObMetaClass

if TYPE_CHECKING:
    from pyob.types import Args, Kwargs, PyObStore


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ PYOB CLASS
# └─────────────────────────────────────────────────────────────────────────────────────


class PyObClass(type):
    """The root metaclass for PyOb and all of its subclasses"""

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ __INIT__
    # └─────────────────────────────────────────────────────────────────────────────────

    def __init__(cls: PyObClass, *args: Args, **kwargs: Kwargs):
        """Init Method"""

        # ┌─────────────────────────────────────────────────────────────────────────────
        # │ PYOB META
        # └─────────────────────────────────────────────────────────────────────────────

        # Retrieve user-defined PyObMeta class
        PyObMeta = getattr(cls, "PyObMeta", {})

        # Get dictionary of user-defined PyObMeta attributes
        pyob_meta_dict = PyObMeta and PyObMeta.__dict__

        # Initialize user-defined PyObMeta into a PyObMetaClass instance
        _PyObMeta = cls._PyObMeta = PyObMetaClass[Any](**pyob_meta_dict)

        # ┌─────────────────────────────────────────────────────────────────────────────
        # │ BASE CLASSES
        # └─────────────────────────────────────────────────────────────────────────────

        # Iterate over child's base classes
        for Base in cls.__bases__:

            # Continue if base class is not a PyObClass
            # i.e. Does not share the child's metaclass, i.e. PyObClass
            if type(Base) is not PyObClass:
                continue

            # ┌─────────────────────────────────────────────────────────────────────────
            # │ PARENTS AND CHILDREN
            # └─────────────────────────────────────────────────────────────────────────

            # Extend to Parents of current PyObMeta
            _PyObMeta.Parents = _PyObMeta.Parents + (Base,)

            # Extend current class to Children of parent PyObMeta
            Base._PyObMeta.Children = Base._PyObMeta.Children + (cls,)

            # ┌─────────────────────────────────────────────────────────────────────────
            # │ FIELD SET INHERITANCE
            # └─────────────────────────────────────────────────────────────────────────

            # Inherit keys from parent
            _PyObMeta.keys = Base._PyObMeta.keys | _PyObMeta.keys

            # Inherit uniques from parent
            _PyObMeta.uniques = Base._PyObMeta.uniques | _PyObMeta.uniques

            # Inherit indexes from parent
            _PyObMeta.indexes = Base._PyObMeta.indexes | _PyObMeta.indexes

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ OBS
    # └─────────────────────────────────────────────────────────────────────────────────

    @property
    def obs(cls) -> PyObStore[Any]:
        """Returns PyObClass._PyObMeta.store"""

        # Return PyObClass.store
        return cls._PyObMeta.store

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ OBJECTS
    # └─────────────────────────────────────────────────────────────────────────────────

    @property
    def objects(cls) -> PyObStore[Any]:
        """Returns PyObClass._PyObMeta.store"""

        # Return PyObClass.store
        return cls._PyObMeta.store
