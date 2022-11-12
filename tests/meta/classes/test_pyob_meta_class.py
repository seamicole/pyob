# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ PROJECT IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from pyob.meta.classes.pyob_meta_class import PyObMetaClass


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ TEST PYOB META CLASS
# └─────────────────────────────────────────────────────────────────────────────────────


class TestPyObMetaClass:
    """A test class for pyob.meta.classes.pyob_meta_class.PyObMetaClass"""

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ TEST INIT CREATES EMPTY LIST OF PARENTS AND CHILDREN
    # └─────────────────────────────────────────────────────────────────────────────────

    def test_init_creates_empty_list_of_parents_and_children(self):
        """Tests that Parents and Children are initialized to an empty list"""

        # Create a PyObMetaClass instance
        PyObMeta = PyObMetaClass()

        # Assert that PyObMeta Parents is an empty list
        assert type(PyObMeta.Parents) is list and len(PyObMeta.Parents) == 0

        # Assert that PyObMeta Parents is an empty list
        assert type(PyObMeta.Children) is list and len(PyObMeta.Children) == 0
