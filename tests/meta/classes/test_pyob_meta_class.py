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

    def test_init_creates_empty_list_of_parents_and_children(self) -> None:
        """Tests that Parents and Children are initialized to an empty list"""

        # Create a PyObMetaClass instance
        PyObMeta = PyObMetaClass()

        # Assert that PyObMeta Parents is an empty list
        assert type(PyObMeta.Parents) is tuple and len(PyObMeta.Parents) == 0

        # Assert that PyObMeta Children is an empty list
        assert type(PyObMeta.Children) is tuple and len(PyObMeta.Children) == 0

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ TEST INIT FREEZES CONSTRAINTS
    # └─────────────────────────────────────────────────────────────────────────────────

    def test_init_freezes_constraints(self) -> None:
        """Tests that constraints passed into the PyObMetaClass instance are frozen"""

        # Create a PyObMetaClass instance without constraints
        UnconstrainedPyObMeta = PyObMetaClass()

        # Assert that PyObMeta uniques is an empty frozenset
        assert UnconstrainedPyObMeta.uniques == frozenset([])

        # Assert that PyObMeta indexes is an empty frozenset
        assert UnconstrainedPyObMeta.indexes == frozenset([])

        # Create another PyObMetaClass instance with constraints
        ConstrainedPyObMeta = PyObMetaClass(
            uniques=("a", "b", ("c", "d", "c"), "a"),
            indexes=("e", "f", ("g", "h", "g"), "e"),
        )

        # Assert that uniques is now a frozenset
        assert type(ConstrainedPyObMeta.uniques) is frozenset

        # Assert that unique fields are correct
        assert ConstrainedPyObMeta.uniques == {"a", "b", frozenset(("c", "d"))}

        # Assert that indexes is now a frozenset
        assert type(ConstrainedPyObMeta.indexes) is frozenset

        # Assert that indexed fields are correct
        assert ConstrainedPyObMeta.indexes == {"e", "f", frozenset(("g", "h"))}
