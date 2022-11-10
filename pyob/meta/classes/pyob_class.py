# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ GENERAL IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from __future__ import annotations
from typing import TYPE_CHECKING

# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ PROJECT IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from pyob.meta.tools.cloners import clone_pyob_meta
from pyob.meta.tools.yielders import yield_parents

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

        # Clone the initial PyObMeta object
        # So that it occupies a different address in memory and therefore does not
        # propogate changes to the PyObMeta class of parent PyOb classes if inherited!
        cls.PyObMeta = clone_pyob_meta(PyObMeta=cls.PyObMeta)

        # Retrieve the newly cloned PyObMeta class
        PyObMeta = cls.PyObMeta

        # ┌─────────────────────────────────────────────────────────────────────────────
        # │ PARENTS AND CHILDREN
        # └─────────────────────────────────────────────────────────────────────────────

        # Initialize list of parent classes
        # i.e. The subset of bases that are also PyObClasses
        PyObMeta.Parents = []

        # Initialize list of child classes
        # i.e. Any PyObClasses that end up inheriting from the current class
        PyObMeta.Children = []

        # Iterate over parents
        for Parent in yield_parents(Child=cls):

            # Append to Parents of current PyObMeta
            PyObMeta.Parents.append(Parent)

            # Append current class to Children of parent PyObMeta
            Parent.PyObMeta.Children.append(cls)

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ PYOB META
    # └─────────────────────────────────────────────────────────────────────────────────

    class PyObMeta:
        """PyObMeta Class"""

        # ┌─────────────────────────────────────────────────────────────────────────────
        # │ RELATIVES
        # └─────────────────────────────────────────────────────────────────────────────

        # Initialize list of parent classes to None
        Parents: list[PyObClass] | None = None

        # Initialize list of child classes to None
        Children: list[PyObClass] | None = None
