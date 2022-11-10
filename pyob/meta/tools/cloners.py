# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ GENERAL IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from typing import Type, TypeVar

# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ PROJECT IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from pyob.meta.classes.pyob_meta_base import PyObMetaBase


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ CLONE PYOB META
# └─────────────────────────────────────────────────────────────────────────────────────

T = TypeVar("T")


def clone_pyob_meta(PyObMeta: Type[T]) -> Type[T]:
    """Clones a PyObMeta such that it occupies a different address in memory"""

    # Get PyObMeta base dictionary
    # i.e. A blank copy of the PyObMetaBase attributes
    # To ensure every PyObMeta class shares a common set of attributes and methods
    pyob_meta_dict = dict(PyObMetaBase.__dict__)

    # Update PyObMeta dictionary with the attributes of the current class PyObMeta
    # To ensure the metaclass dictionary inherits all the attributes and methods
    # defined in the current class PyObMeta
    pyob_meta_dict.update(dict(PyObMeta.__dict__))

    # Create a new reference for PyObMeta so each PyOb class has its own PyObMeta
    # Otherwise we will end up reassigning mutable attributes such as the store
    PyObMeta = type("PyObMeta", PyObMeta.__bases__, pyob_meta_dict)

    # Return the freshly initialized PyObMeta
    return PyObMeta
