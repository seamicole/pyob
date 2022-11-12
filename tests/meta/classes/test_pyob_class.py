# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ PROJECT IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from pyob.main.classes.pyob import PyOb
from pyob.meta.classes.pyob_meta_class import PyObMetaClass


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

        # Define a parent PyOb class
        class ParentOne(PyOb):
            """A dummy parent PyOb class"""

        # Assert that the parent of ParentOne is PyOb
        assert (
            len(ParentOne.PyObMeta.Parents) == 1
            and ParentOne.PyObMeta.Parents[0] is PyOb
        )

        # Define a child PyOb class
        class ChildOne(ParentOne):
            """A dummy child PyOb class"""

        # Assert that the parent of ChildOne is ParentOne
        assert (
            len(ChildOne.PyObMeta.Parents) == 1
            and ChildOne.PyObMeta.Parents[0] is ParentOne
        )

        # Define another parent PyOb class
        class ParentTwo(PyOb):
            """A dummy parent PyOb class"""

        # Define another child PyOb class that inherits from both parents
        class ChildTwo(ParentOne, ParentTwo):
            """A dummy child PyOb class"""

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

        # Define a parent PyOb class
        class ParentOne(PyOb):
            """A dummy parent PyOb class"""

        # Assert that PyOb now has one more child
        assert (
            len(PyOb.PyObMeta.Children) == pyob_child_count_initial + 1
            and ParentOne in PyOb.PyObMeta.Children
        )

        # Assert that ParentOne has no children
        assert len(ParentOne.PyObMeta.Children) == 0

        # Define a child PyOb class
        class ChildOne(ParentOne):
            """A dummy child PyOb class"""

        # Assert that ParentOne now has one child
        assert (
            len(ParentOne.PyObMeta.Children) == 1
            and ParentOne.PyObMeta.Children[0] is ChildOne
        )

        # Assert that ChildOne has no children
        assert len(ChildOne.PyObMeta.Children) == 0

        # Define another parent PyOb class
        class ParentTwo(PyOb):
            """A dummy parent PyOb class"""

        # Assert that PyOb now has one more child
        assert (
            len(PyOb.PyObMeta.Children) == pyob_child_count_initial + 2
            and ParentOne in PyOb.PyObMeta.Children
            and ParentTwo in PyOb.PyObMeta.Children
        )

        # Assert that ParentTwo has no children
        assert len(ParentTwo.PyObMeta.Children) == 0

        # Define another child PyOb class that inherits from ParentOne and ParentTwo
        class ChildTwo(ParentOne, ParentTwo):
            """A dummy child PyOb class"""

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
