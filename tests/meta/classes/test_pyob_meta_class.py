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
    # │ TEST INIT CREATES EMPTY TUPLE OF PARENTS AND CHILDREN
    # └─────────────────────────────────────────────────────────────────────────────────

    def test_init_creates_empty_tuple_of_parents_and_children(self) -> None:
        """Tests that Parents and Children are initialized to an empty tuple"""

        # Create a PyObMetaClass instance
        PyObMeta = PyObMetaClass()

        # Assert that PyObMeta Parents is an empty tuple
        assert type(PyObMeta.Parents) is tuple and len(PyObMeta.Parents) == 0

        # Assert that PyObMeta Children is an empty tuple
        assert type(PyObMeta.Children) is tuple and len(PyObMeta.Children) == 0

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ TEST INIT FREEZES FIELD SETS
    # └─────────────────────────────────────────────────────────────────────────────────

    def test_init_freezes_field_sets(self) -> None:
        """Tests that field sets passed into the PyObMetaClass instance are frozen"""

        # Create a PyObMetaClass instance without constraints
        UnconstrainedPyObMeta = PyObMetaClass()

        # Assert that PyObMeta keys is an empty frozenset
        assert UnconstrainedPyObMeta.keys == frozenset([])

        # Assert that PyObMeta uniques is an empty frozenset
        assert UnconstrainedPyObMeta.uniques == frozenset([])

        # Assert that PyObMeta indexes is an empty frozenset
        assert UnconstrainedPyObMeta.indexes == frozenset([])

        # Create another PyObMetaClass instance with constraints
        ConstrainedPyObMeta = PyObMetaClass(
            keys=("a", "b", ("c", "d", "c"), "a"),
            uniques=("e", "f", ("g", "h", "g"), "e"),
            indexes=("i", "j", ("k", "l", "k"), "i"),
        )

        # Assert that keys is now a frozenset
        assert type(ConstrainedPyObMeta.keys) is frozenset

        # Assert that key fields are correct
        assert ConstrainedPyObMeta.keys == {"a", "b", frozenset(("c", "d"))}

        # Assert that uniques is now a frozenset
        assert type(ConstrainedPyObMeta.uniques) is frozenset

        # Assert that unique fields are correct
        assert ConstrainedPyObMeta.uniques == ConstrainedPyObMeta.keys | {
            "e",
            "f",
            frozenset(("g", "h")),
        }

        # Assert that indexes is now a frozenset
        assert type(ConstrainedPyObMeta.indexes) is frozenset

        # Assert that indexed fields are correct
        assert ConstrainedPyObMeta.indexes == {"i", "j", frozenset(("k", "l"))}

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ TEST INIT INCLUDES KEYS IN UNIQUES
    # └─────────────────────────────────────────────────────────────────────────────────

    def test_init_includes_keys_in_uniques(self) -> None:
        """Tests that keys are always unique by definition"""

        # Create a PyObMetaClass instance
        PyObMeta = PyObMetaClass(keys=("a", "b", "c"), uniques=("c", "d", "e"))

        # Assert that uniques include keys automatically
        assert PyObMeta.uniques == frozenset(("a", "b", "c", "d", "e"))
