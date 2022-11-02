# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ PROJECT IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from pyob.meta.classes.pyob_meta_base import PyObMetaBase
from pyob.meta.tools.clone import clone_pyob_meta


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ TEST CLONE PYOB META
# └─────────────────────────────────────────────────────────────────────────────────────


def test_is_clone_pyob_meta() -> None:
    """Tests that a PyObMeta class is properly cloned into a new object in memory"""

    # Define a new PyObMeta class
    class PyObMetaDummy:
        """A dummy PyObMeta class"""

        # Initialize keys to None
        keys = ("key", "name")

        # Initialize string field
        string = "name"

        # Initialize labels to None
        label_singular = "Dummy"
        label_plural = "Dummies"

    # Get the original PyObMeta object ID
    pyob_meta_id = id(PyObMetaDummy)

    # Clone the PyObMeta class
    ClonedPyObMetaDummy = clone_pyob_meta(PyObMetaDummy)

    # Get the clones PyObMeta object ID
    cloned_pyob_meta_id = id(ClonedPyObMetaDummy)

    # Assert that the two PyObMeta classes occupy two different addresses in memory
    assert pyob_meta_id != cloned_pyob_meta_id

    # Define exceptions
    exceptions = {"Parents", "Children"}

    # Iterate over attributes in PyObMetaBase class
    for attribute in PyObMetaBase.__dict__:

        # Continue if an exception
        if attribute in exceptions:
            continue

        # Assert that the attribtes in both PyObMeta classes are identical
        PyObMetaDummy.__dict__[attribute] == ClonedPyObMetaDummy.__dict__[attribute]
