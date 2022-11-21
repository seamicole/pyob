# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ GENERAL IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from __future__ import annotations

from typing import TYPE_CHECKING

# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ PROJECT IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from pyob.meta.classes.pyob_meta_class import PyObMetaClass

if TYPE_CHECKING:
    from pyob.types import Args, Kwargs


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
        # Ignore type checks to allow reassigning of PyObMeta to PyObMetaClass instance
        PyObMeta = cls.PyObMeta = PyObMetaClass(**pyob_meta_dict)

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
            PyObMeta.Parents = PyObMeta.Parents + (Base,)

            # Extend current class to Children of parent PyObMeta
            Base.PyObMeta.Children = Base.PyObMeta.Children + (cls,)

            # ┌─────────────────────────────────────────────────────────────────────────
            # │ FIELD SET INHERITANCE
            # └─────────────────────────────────────────────────────────────────────────

            # Inherit keys from parent
            PyObMeta.keys = Base.PyObMeta.keys | PyObMeta.keys

            # Inherit uniques from parent
            PyObMeta.uniques = Base.PyObMeta.uniques | PyObMeta.uniques

            # Inherit indexes from parent
            PyObMeta.indexes = Base.PyObMeta.indexes | PyObMeta.indexes

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ STORE
    # └─────────────────────────────────────────────────────────────────────────────────

    @property
    def store(cls):
        """Returns PyObClass.PyObMeta.store"""

        # Return PyObClass.PyObMeta.store
        return cls.PyObMeta.store

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ OBS
    # └─────────────────────────────────────────────────────────────────────────────────

    @property
    def obs(cls):
        """Returns PyObClass.PyObMeta.store"""

        # Return PyObClass.store
        return cls.PyObMeta.store

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ OBJECTS
    # └─────────────────────────────────────────────────────────────────────────────────

    @property
    def objects(cls):
        """Returns PyObClass.PyObMeta.store"""

        # Return PyObClass.store
        return cls.PyObMeta.store
