# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ PROJECT IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from pyob import PyOb
from pyob.meta.tools.create import create_label_plural, create_label_singular


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ TEST CREATE LABEL SINGULAR
# └─────────────────────────────────────────────────────────────────────────────────────


def test_create_label_singular() -> None:
    """Tests that a singular label can be derived from a PyOb class name as expected"""

    # Define a dummy PyOb class
    class PyObClassDummy(PyOb):
        """A dummy PyOb class"""

    # Get singular label
    label_singular = create_label_singular(PyObClass=PyObClassDummy)

    # Assert that the singular label is the Pascalized version of PyObClass.__name__
    assert label_singular == "Py Ob Class Dummy"


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ TEST CREATE LABEL PLURAL
# └─────────────────────────────────────────────────────────────────────────────────────


def test_create_label_plural() -> None:
    """Tests that a plural label can be derived from a PyOb class name as expected"""

    # Define a dummy PyOb class
    class PyObClassDummy(PyOb):
        """A dummy PyOb class"""

    # Get plural label
    label_plural = create_label_plural(PyObClass=PyObClassDummy)

    # Assert that the plural label derives from the singular label
    assert label_plural == "Py Ob Class Dummies"

    # Define another dummy PyOb class
    class PyObClassDummy(PyOb):
        """A dummy PyOb class"""

        class PyObMeta:
            """PyObMeta Class"""

            # Define a singular label
            label_singular = "Dummy"

    # Get plural label
    label_plural = create_label_plural(PyObClass=PyObClassDummy)

    # Assert that the plural label still derives from the custom singular label
    assert label_plural == "Dummies"
