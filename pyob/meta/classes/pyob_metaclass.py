# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ GENERAL IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

import inflect

# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ PROJECT IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from pyob.meta.tools.clone import clone_pyob_meta
from pyob.store.classes.pyob_store import PyObStore
from pyob.tools.check import is_pyob_store_instance
from pyob.tools.string import split_pascal


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ PYOB METACLASS
# └─────────────────────────────────────────────────────────────────────────────────────


class PyObMetaclass(type):
    """The root metaclass for all PyOb subclasses"""

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ __INIT__
    # └─────────────────────────────────────────────────────────────────────────────────

    def __init__(cls, *args, **kwargs):
        """Init Method"""

        # ┌─────────────────────────────────────────────────────────────────────────────
        # │ PYOB META
        # └─────────────────────────────────────────────────────────────────────────────

        # Record the initial PyObMeta object ID
        # To compare against parent PyObMeta classes below
        # Some attributes such as labels should not be inherited!
        initial_pyob_meta_id = id(cls.PyObMeta)

        # Clone the initial PyObMeta object
        # So that it occupies a different address in memory and therefore does not
        # propogate changes to the PyObMeta class of parent PyOb classes if inherited!
        cls.PyObMeta = clone_pyob_meta(cls.PyObMeta)

        # Retrieve the newly cloned PyObMeta class
        PyObMeta = cls.PyObMeta

        # ┌─────────────────────────────────────────────────────────────────────────────
        # │ PYOB STORE
        # └─────────────────────────────────────────────────────────────────────────────

        # Initialize the PyOb store
        # i.e. The "database" of all instances initialized from the current PyOb class
        PyObMeta.store = PyObStore(PyObClass=cls)

        # ┌─────────────────────────────────────────────────────────────────────────────
        # │ RELATIVES
        # └─────────────────────────────────────────────────────────────────────────────

        # Initialize list of parent classes
        # i.e. The subset of bases that are also PyOb classes
        PyObMeta.Parents = []

        # Initialize list of child classes
        # i.e. Any PyOb classes that end up inheriting from the current class
        PyObMeta.Children = []

        # Iterate over all base classes
        for Base in cls.__bases__:

            # Get PyObMeta of base class
            # i.e. Most likely a PyOb class if PyObMeta is not None
            ParentPyObMeta = getattr(Base, "PyObMeta", None)

            # Get store of base PyObMeta class if not None
            parent_store = ParentPyObMeta and getattr(ParentPyObMeta, "store", None)

            # Continue if parent PyObMeta store is not a PyOb store
            # i.e. Definitely not a PyOb class
            if not is_pyob_store_instance(parent_store):
                continue

            # Add base class to Parents of current PyObMeta class
            PyObMeta.Parents.append(Base)

            # Add current class to Children of parent PyObMeta class
            ParentPyObMeta.Children.append(cls)

            # Check if the parent PyOb meta ID is being used for the current PyOb class
            if id(ParentPyObMeta) == initial_pyob_meta_id:

                # Nullify label fields
                # If the current PyOb class does not define a PyObMeta class
                # do NOT inherit labels from the parent PyObMeta class
                PyObMeta.label_singular = None
                PyObMeta.label_plural = None

        # ┌─────────────────────────────────────────────────────────────────────────────
        # │ PYOB CLASS SINGULAR LABEL
        # └─────────────────────────────────────────────────────────────────────────────

        # Get singular label from PyObMeta
        label_singular = PyObMeta.label_singular

        # Check if singular label is null
        if not label_singular:

            # Default singular label to derivative of Class.__name__
            label_singular = " ".join(split_pascal(cls.__name__))

            # Strip singular label
            label_singular = label_singular.strip()

            # Set singular label on PyObMeta
            PyObMeta.label_singular = label_singular

        # ┌─────────────────────────────────────────────────────────────────────────────
        # │ PYOB CLASS PLURAL LABEL
        # └─────────────────────────────────────────────────────────────────────────────

        # Get plural label from PyObMeta
        label_plural = PyObMeta.label_plural

        # Check if plural label is null
        if not label_plural:

            # Initialize inflector
            inflector = inflect.engine()

            # Pluralize the singular label
            label_plural = inflector.plural(label_singular)

            # Set plural label on PyObMeta
            PyObMeta.label_plural = label_plural
