# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ PROJECT IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from pyob.main.classes.pyob import PyOb
from pyob.meta.classes.pyob_meta_class import PyObMetaClass
from pyob.store.classes.pyob_store import PyObStore


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ TEST PYOB CLASS
# └─────────────────────────────────────────────────────────────────────────────────────


class TestPyObClass:
    """A test class for pyob.meta.classes.pyob_class.PyObClass"""

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ TEST INIT CREATES PYOB META CLASS INSTANCE
    # └─────────────────────────────────────────────────────────────────────────────────

    def test_init_creates_pyob_meta_class_instance(self) -> None:
        """Tests that a PyObMeta class is initialized when the PyObClass is defined"""

        # Assert PyOb.PyObMeta is an instance of PyObClass
        assert isinstance(PyOb.PyObMeta, PyObMetaClass)

        # Define a PyObClass with an inherited PyObMeta
        class InheritedPyObMeta(PyOb):
            """A dummy PyObClass whose PyObMeta is inherited from PyOb"""

        # Assert InheritedPyObMeta.PyObMeta is an instance of PyObClass
        assert isinstance(InheritedPyObMeta.PyObMeta, PyObMetaClass)

        # Define a PyObClass with a redefined PyObMeta
        class RedefinedPyObMeta(PyOb):
            """A dummy PyObClass whose PyObMeta is redefined by the user"""

            class PyObMeta:
                """PyObMeta Class"""

        # Assert RedefinedPyObMeta.PyObMeta is an instance of PyObClass
        assert isinstance(RedefinedPyObMeta.PyObMeta, PyObMetaClass)

        # Assert that each of the above PyObMeta instances are distinct in memory
        assert (
            id(PyOb.PyObMeta) != id(InheritedPyObMeta.PyObMeta) != id(RedefinedPyObMeta)
        )

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ TEST INIT ASSIGNS PARENTS
    # └─────────────────────────────────────────────────────────────────────────────────

    def test_init_assigns_parents(self) -> None:
        """Tests that PyOb parent classes are assigned to a PyObClass when defined"""

        # Assert that PyOb has no parent classes
        assert len(PyOb.PyObMeta.Parents) == 0

        # Define a parent PyObClass
        class ParentOne(PyOb):
            """A dummy parent PyObClass"""

        # Assert that the parent of ParentOne is PyOb
        assert (
            len(ParentOne.PyObMeta.Parents) == 1
            and ParentOne.PyObMeta.Parents[0] is PyOb
        )

        # Define a child PyObClass
        class ChildOne(ParentOne):
            """A dummy child PyObClass"""

        # Assert that the parent of ChildOne is ParentOne
        assert (
            len(ChildOne.PyObMeta.Parents) == 1
            and ChildOne.PyObMeta.Parents[0] is ParentOne
        )

        # Define another parent PyObClass
        class ParentTwo(PyOb):
            """A dummy parent PyObClass"""

        # Define another child PyObClass that inherits from both parents
        class ChildTwo(ParentOne, ParentTwo):
            """A dummy child PyObClass"""

        # Assert that the parents of ChildTwo is ParentOne and ParentTwo
        assert (
            len(ChildTwo.PyObMeta.Parents) == 2
            and ChildTwo.PyObMeta.Parents[0] is ParentOne
            and ChildTwo.PyObMeta.Parents[1] is ParentTwo
        )

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ TEST INIT ASSIGNS CHILDREN
    # └─────────────────────────────────────────────────────────────────────────────────

    def test_init_assigns_children(self) -> None:
        """
        Tests that PyOb child classes are assigned to a PyObClass parent classes when
        defined
        """

        # Get initial number of PyOb children
        pyob_child_count_initial = len(PyOb.PyObMeta.Children)

        # Define a parent PyObClass
        class ParentOne(PyOb):
            """A dummy parent PyObClass"""

        # Assert that PyOb now has one more child
        assert (
            len(PyOb.PyObMeta.Children) == pyob_child_count_initial + 1
            and ParentOne in PyOb.PyObMeta.Children
        )

        # Assert that ParentOne has no children
        assert len(ParentOne.PyObMeta.Children) == 0

        # Define a child PyObClass
        class ChildOne(ParentOne):
            """A dummy child PyObClass"""

        # Assert that ParentOne now has one child
        assert (
            len(ParentOne.PyObMeta.Children) == 1
            and ParentOne.PyObMeta.Children[0] is ChildOne
        )

        # Assert that ChildOne has no children
        assert len(ChildOne.PyObMeta.Children) == 0

        # Define another parent PyObClass
        class ParentTwo(PyOb):
            """A dummy parent PyObClass"""

        # Assert that PyOb now has one more child
        assert (
            len(PyOb.PyObMeta.Children) == pyob_child_count_initial + 2
            and ParentOne in PyOb.PyObMeta.Children
            and ParentTwo in PyOb.PyObMeta.Children
        )

        # Assert that ParentTwo has no children
        assert len(ParentTwo.PyObMeta.Children) == 0

        # Define another child PyObClass that inherits from ParentOne and ParentTwo
        class ChildTwo(ParentOne, ParentTwo):
            """A dummy child PyObClass"""

        # Assert that ParentOne now has two children
        assert (
            len(ParentOne.PyObMeta.Children) == 2
            and ParentOne.PyObMeta.Children[0] is ChildOne
            and ParentOne.PyObMeta.Children[1] is ChildTwo
        )

        # Assert that ParentTwo now has one child
        assert (
            len(ParentTwo.PyObMeta.Children) == 1
            and ParentTwo.PyObMeta.Children[0] is ChildTwo
        )

        # Assert that ChildTwo has no children
        assert len(ChildTwo.PyObMeta.Children) == 0

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ TEST INIT RESPECTS CUSTOM PYOB STORE CLASSES
    # └─────────────────────────────────────────────────────────────────────────────────

    def test_init_respects_custom_pyob_store_classes(self) -> None:
        """Tests that a user can define a custom PyObStore class in PyObMeta"""

        # Define a PyObClass with a default PyObStore
        class DefaultPyObClass(PyOb):
            """A dummy PyObClass"""

        # Assert that the DefaultPyObClass.PyObMeta is initialized with a PyObStore
        assert type(DefaultPyObClass.PyObMeta.store) is PyObStore

        # Define a custom PyObStore class
        class CustomStore(PyObStore):
            """A dummy PyObStore"""

        # Define a PyObClass with a custom PyObStore
        class CustomPyObClass(PyOb):
            """A dummy PyObClass"""

            class PyObMeta:
                """PyObMeta Class"""

                Store = CustomStore

        # Assert that the CustomPyObClass.PyObMeta is initialized with a CustomStore
        assert type(CustomPyObClass.PyObMeta.store) is CustomStore

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ TEST INIT INHERITS FIELD SETS
    # └─────────────────────────────────────────────────────────────────────────────────

    def test_init_inherits_field_sets(self) -> None:
        """Tests that field sets are passed on from parent to child classes"""

        # Define a parent PyObClass
        class ParentOne(PyOb):
            """A dummy parent PyObClass"""

            class PyObMeta:

                # Using sets here because mypy complains otherwise
                keys = {"a1", "b1", "c1"}
                uniques = {"d1", "e1", "f1"}
                indexes = {"g1", "h1", "i1"}

        # Define a child PyObClass
        class ChildOne(ParentOne):
            """A dummy child PyObClass"""

        # Assert that ChildOne inherits ParentOne's field sets
        assert ChildOne.PyObMeta.keys == ParentOne.PyObMeta.keys
        assert ChildOne.PyObMeta.uniques == ParentOne.PyObMeta.uniques
        assert ChildOne.PyObMeta.indexes == ParentOne.PyObMeta.indexes

        # Define another child PyObClass
        class ChildTwo(ParentOne):
            """A dummy child PyObClass"""

            class PyObMeta:

                keys = ("aa2", "bb2", "cc2")
                uniques = ("dd2", "ee2", "ff2")
                indexes = ("gg2", "hh2", "ii2")

        # Assert that ChildOne inherits ParentOne's field sets
        assert ChildTwo.PyObMeta.keys == ParentOne.PyObMeta.keys | {"aa2", "bb2", "cc2"}
        assert ChildTwo.PyObMeta.uniques == ParentOne.PyObMeta.uniques | {
            # Keys
            "aa2",
            "bb2",
            "cc2",
            # Uniques
            "dd2",
            "ee2",
            "ff2",
        }
        assert ChildTwo.PyObMeta.indexes == ParentOne.PyObMeta.indexes | {
            "gg2",
            "hh2",
            "ii2",
        }

        # Define another parent PyObClass
        class ParentTwo(PyOb):
            """A dummy parent PyObClass"""

            class PyObMeta:

                # Using sets here because mypy complains otherwise
                keys = {"a2", "b2", "c2"}
                uniques = {"d2", "e2", "f2"}
                indexes = {"g2", "h2", "i2"}

        # Define another child PyObClass
        class ChildThree(ParentOne, ParentTwo):
            """A dummy child PyObClass"""

            class PyObMeta:

                keys = ("aa3", "bb3", "cc3")
                uniques = ("dd3", "ee3", "ff3")
                indexes = ("gg3", "hh3", "ii3")

        # Assert that ChildOne inherits ParentOne and ParentTwo's field sets
        assert (
            ChildThree.PyObMeta.keys
            == ParentOne.PyObMeta.keys | ParentTwo.PyObMeta.keys | {"aa3", "bb3", "cc3"}
        )
        assert (
            ChildThree.PyObMeta.uniques
            == ParentOne.PyObMeta.uniques
            | ParentTwo.PyObMeta.uniques
            | {
                # Keys
                "aa3",
                "bb3",
                "cc3",
                # Uniques
                "dd3",
                "ee3",
                "ff3",
            }
        )
        assert (
            ChildThree.PyObMeta.indexes
            == ParentOne.PyObMeta.indexes
            | ParentTwo.PyObMeta.indexes
            | {
                "gg3",
                "hh3",
                "ii3",
            }
        )

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ TEST STORE PROPERTY POINTS TO PYOB META STORE
    # └─────────────────────────────────────────────────────────────────────────────────

    def test_store_property_points_to_pyob_meta_store(self) -> None:
        """Tests that the store property points to PyObClass.PyObMeta.store"""

        # Define a dummy PyObClass
        class DummyClass(PyOb):
            """A dummy PyObClass"""

        # Assert that DummyClass.store points to DummyClass.PyObMeta.store
        assert id(DummyClass.store) == id(DummyClass.PyObMeta.store)

        # Assert that DummyClass.obs points to DummyClass.PyObMeta.store
        assert id(DummyClass.obs) == id(DummyClass.PyObMeta.store)

        # Assert that DummyClass.objects points to DummyClass.PyObMeta.store
        assert id(DummyClass.objects) == id(DummyClass.PyObMeta.store)
