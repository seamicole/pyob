# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ PROJECT IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from pyob.meta.tools.clone import clone_pyob_meta
from pyob.meta.tools.create import create_label_plural, create_label_singular
from pyob.store.classes.pyob_store import PyObStore
from pyob.tools.check import is_pyob_store_instance, is_type
from pyob.tools.sequence import deduplicate
from pyob.types import Key, Keys


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
                # DO NOT inherit labels from the parent PyObMeta class
                # Labels should default to the current Class.__name__
                PyObMeta.label_singular = None
                PyObMeta.label_plural = None

        # NOTE: The above logic contains various side effects and is therefore not
        # modularized into a separate helper function!

        # ┌─────────────────────────────────────────────────────────────────────────────
        # │ KEYS
        # └─────────────────────────────────────────────────────────────────────────────

        # Get key from current PyObMeta
        # Not a native PyObMeta attribute
        # Can be used as a user-facing shortcut
        key = getattr(PyObMeta, "key", ())

        # Assert that key is a tuple of strings
        is_type(
            key,
            Key | Keys,
            raise_if=False,
            message="PyObClass.PyObMeta.key expects a string!",
        )

        # Convert key to a tuple of strings
        key = (key,) if type(key) is str else tuple(key)

        # Get keys from current PyObMeta
        keys = PyObMeta.keys or ()

        # Assert that keys is a tuple of strings
        is_type(
            keys,
            Key | Keys,
            raise_if=False,
            message="PyObClass.PyObMeta.keys expects a tuple of strings!",
        )

        # Ensure that keys is a tuple of strings
        keys = (keys,) if type(keys) is str else tuple(keys)

        # Combine keys
        keys = key + keys

        # Merge parent PyObMeta keys into current PyObMeta keys
        # This ensures that all PyOb subclasses inherit their parents' keys
        keys = sum([Parent.PyObMeta.keys for Parent in PyObMeta.Parents] + [keys], ())

        # Remove any duplicate keys
        keys = deduplicate(keys)

        # Set PyObMeta.keys
        PyObMeta.keys = keys

        # ┌─────────────────────────────────────────────────────────────────────────────
        # │ LABELS
        # └─────────────────────────────────────────────────────────────────────────────

        # Initialize singular label
        PyObMeta.label_singular = PyObMeta.label_singular or create_label_singular(
            PyObClass=cls
        )

        # Initialize plural label
        PyObMeta.label_plural = PyObMeta.label_plural or create_label_plural(
            PyObClass=cls
        )
