# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ GENERAL IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

import pytest

from abc import ABCMeta, abstractmethod

# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ PROJECT IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from pyob.main.classes.pyob import PyOb
from pyob.meta.classes.pyob_class import PyObClass
from pyob.meta.classes.pyob_meta_class import PyObMetaClass


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ TEST PYOB CLASS
# └─────────────────────────────────────────────────────────────────────────────────────


class TestPyObClass:
    """A test class for pyob.meta.classes.pyob_class.PyObClass"""

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ TEST PYOB CLASS SUBCLASSES ABCMETA
    # └─────────────────────────────────────────────────────────────────────────────────

    def test_pyob_class_subclasses_abc_meta(self) -> None:
        """Tests that the PyOb class metaclass is a subclass of ABCMeta"""

        # Assert PyObClass subclasses ABCMeta
        assert issubclass(PyObClass, ABCMeta)

        # Define a dummy PyOb class without an abstract method
        class WithoutAbstractMethod(PyOb):
            """A dummy PyOb class with no abstract methods"""

            def standard_method(self) -> bool:
                return True

        # Assert that a PyOb class without an abstract method can be initialized
        assert WithoutAbstractMethod().standard_method() is True

        # Define a dummy PyOb class with an abstract method
        class WithAbstractMethod(PyOb):
            """A dummy PyOb class with an abstract method"""

            @abstractmethod
            def abstract_method(self) -> None:
                """An abstract method"""

        # Initialize raises block
        with pytest.raises(TypeError):

            # Try to initialize a dummy class with an abstract method
            WithAbstractMethod()  # type: ignore

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ TEST INIT CREATES PYOB META CLASS INSTANCE
    # └─────────────────────────────────────────────────────────────────────────────────

    def test_init_creates_pyob_meta_class_instance(self) -> None:
        """Tests that a PyObMeta class is initialized when the PyOb class is defined"""

        # Assert PyOb._PyObMeta is an instance of PyObClass
        assert type(PyOb._PyObMeta) is PyObMetaClass

        # Define a PyOb class with an inherited PyObMeta
        class InheritedPyObMeta(PyOb):
            """A dummy PyOb class whose PyObMeta is inherited from PyOb"""

        # Assert InheritedPyObMeta._PyObMeta is an instance of PyObClass
        assert type(InheritedPyObMeta._PyObMeta) is PyObMetaClass

        # Define a PyOb class with a redefined PyObMeta
        class RedefinedPyObMeta(PyOb):
            """A dummy PyOb class whose PyObMeta is redefined by the user"""

            class PyObMeta:
                """PyObMeta Class"""

        # Assert RedefinedPyObMeta._PyObMeta is an instance of PyObClass
        assert type(RedefinedPyObMeta._PyObMeta) is PyObMetaClass

        # Assert that each of the above PyObMeta instances are distinct in memory
        assert (
            id(PyOb._PyObMeta)
            != id(InheritedPyObMeta._PyObMeta)
            != id(RedefinedPyObMeta)
        )

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ TEST INIT ASSIGNS PARENTS
    # └─────────────────────────────────────────────────────────────────────────────────

    def test_init_assigns_parents(self) -> None:
        """Tests that PyOb parent classes are assigned to a PyOb class when defined"""

        # Assert that PyOb has no parent classes
        assert len(PyOb._PyObMeta.Parents) == 0

        # Define a parent PyOb class
        class ParentOne(PyOb):
            """A dummy parent PyOb class"""

        # Assert that the parent of ParentOne is PyOb
        assert (
            len(ParentOne._PyObMeta.Parents) == 1
            and ParentOne._PyObMeta.Parents[0] is PyOb
        )

        # Define a child PyOb class
        class ChildOne(ParentOne):
            """A dummy child PyOb class"""

        # Assert that the parent of ChildOne is ParentOne
        assert (
            len(ChildOne._PyObMeta.Parents) == 1
            and ChildOne._PyObMeta.Parents[0] is ParentOne
        )

        # Define another parent PyOb class
        class ParentTwo(PyOb):
            """A dummy parent PyOb class"""

        # Define another child PyOb class that inherits from both parents
        class ChildTwo(ParentOne, ParentTwo):
            """A dummy child PyOb class"""

        # Assert that the parents of ChildTwo is ParentOne and ParentTwo
        assert (
            len(ChildTwo._PyObMeta.Parents) == 2
            and ChildTwo._PyObMeta.Parents[0] is ParentOne
            and ChildTwo._PyObMeta.Parents[1] is ParentTwo
        )

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ TEST INIT ASSIGNS CHILDREN
    # └─────────────────────────────────────────────────────────────────────────────────

    def test_init_assigns_children(self) -> None:
        """
        Tests that PyOb child classes are assigned to parent classes when defined
        """

        # Get initial number of PyOb children
        pyob_child_count_initial = len(PyOb._PyObMeta.Children)

        # Define a parent PyOb class
        class ParentOne(PyOb):
            """A dummy parent PyOb class"""

        # Assert that PyOb now has one more child
        assert (
            len(PyOb._PyObMeta.Children) == pyob_child_count_initial + 1
            and ParentOne in PyOb._PyObMeta.Children
        )

        # Assert that ParentOne has no children
        assert len(ParentOne._PyObMeta.Children) == 0

        # Define a child PyOb class
        class ChildOne(ParentOne):
            """A dummy child PyOb class"""

        # Assert that ParentOne now has one child
        assert (
            len(ParentOne._PyObMeta.Children) == 1
            and ParentOne._PyObMeta.Children[0] is ChildOne
        )

        # Assert that ChildOne has no children
        assert len(ChildOne._PyObMeta.Children) == 0

        # Define another parent PyOb class
        class ParentTwo(PyOb):
            """A dummy parent PyOb class"""

        # Assert that PyOb now has one more child
        assert (
            len(PyOb._PyObMeta.Children) == pyob_child_count_initial + 2
            and ParentOne in PyOb._PyObMeta.Children
            and ParentTwo in PyOb._PyObMeta.Children
        )

        # Assert that ParentTwo has no children
        assert len(ParentTwo._PyObMeta.Children) == 0

        # Define another child PyOb class that inherits from ParentOne and ParentTwo
        class ChildTwo(ParentOne, ParentTwo):
            """A dummy child PyOb class"""

        # Assert that ParentOne now has two children
        assert (
            len(ParentOne._PyObMeta.Children) == 2
            and ParentOne._PyObMeta.Children[0] is ChildOne
            and ParentOne._PyObMeta.Children[1] is ChildTwo
        )

        # Assert that ParentTwo now has one child
        assert (
            len(ParentTwo._PyObMeta.Children) == 1
            and ParentTwo._PyObMeta.Children[0] is ChildTwo
        )

        # Assert that ChildTwo has no children
        assert len(ChildTwo._PyObMeta.Children) == 0

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ TEST INIT INHERITS FIELD SETS
    # └─────────────────────────────────────────────────────────────────────────────────

    def test_init_inherits_field_sets(self) -> None:
        """Tests that field sets are passed on from parent to child classes"""

        # Define a parent PyOb class
        class ParentOne(PyOb):
            """A dummy parent PyOb class"""

            class PyObMeta:

                # Using sets here because mypy complains otherwise
                keys = {"a1", "b1", "c1"}
                uniques = {"d1", "e1", "f1"}
                indexes = {"g1", "h1", "i1"}

        # Define a child PyOb class
        class ChildOne(ParentOne):
            """A dummy child PyOb class"""

        # Assert that ChildOne inherits ParentOne's field sets
        assert ChildOne._PyObMeta.keys == ParentOne._PyObMeta.keys
        assert ChildOne._PyObMeta.uniques == ParentOne._PyObMeta.uniques
        assert ChildOne._PyObMeta.indexes == ParentOne._PyObMeta.indexes

        # Define another child PyOb class
        class ChildTwo(ParentOne):
            """A dummy child PyOb class"""

            class PyObMeta:

                keys = ("aa2", "bb2", "cc2")
                uniques = ("dd2", "ee2", "ff2")
                indexes = ("gg2", "hh2", "ii2")

        # Assert that ChildOne inherits ParentOne's field sets
        assert ChildTwo._PyObMeta.keys == ParentOne._PyObMeta.keys | {
            "aa2",
            "bb2",
            "cc2",
        }
        assert ChildTwo._PyObMeta.uniques == ParentOne._PyObMeta.uniques | {
            # Keys
            "aa2",
            "bb2",
            "cc2",
            # Uniques
            "dd2",
            "ee2",
            "ff2",
        }
        assert ChildTwo._PyObMeta.indexes == ParentOne._PyObMeta.indexes | {
            "gg2",
            "hh2",
            "ii2",
        }

        # Define another parent PyOb class
        class ParentTwo(PyOb):
            """A dummy parent PyOb class"""

            class PyObMeta:

                # Using sets here because mypy complains otherwise
                keys = {"a2", "b2", "c2"}
                uniques = {"d2", "e2", "f2"}
                indexes = {"g2", "h2", "i2"}

        # Define another child PyOb class
        class ChildThree(ParentOne, ParentTwo):
            """A dummy child PyOb class"""

            class PyObMeta:

                keys = ("aa3", "bb3", "cc3")
                uniques = ("dd3", "ee3", "ff3")
                indexes = ("gg3", "hh3", "ii3")

        # Assert that ChildOne inherits ParentOne and ParentTwo's field sets
        assert (
            ChildThree._PyObMeta.keys
            == ParentOne._PyObMeta.keys
            | ParentTwo._PyObMeta.keys
            | {"aa3", "bb3", "cc3"}
        )
        assert (
            ChildThree._PyObMeta.uniques
            == ParentOne._PyObMeta.uniques
            | ParentTwo._PyObMeta.uniques
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
            ChildThree._PyObMeta.indexes
            == ParentOne._PyObMeta.indexes
            | ParentTwo._PyObMeta.indexes
            | {
                "gg3",
                "hh3",
                "ii3",
            }
        )

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ TEST OBJECTS PROPERTIES POINT TO PYOB META STORE
    # └─────────────────────────────────────────────────────────────────────────────────

    def test_objects_properties_point_to_pyob_meta_store(self) -> None:
        """Tests that the objects properties point to PyObClass._PyObMeta.store"""

        # Define a dummy PyOb class
        class DummyClass(PyOb):
            """A dummy PyOb class"""

        # Assert that DummyClass.obs points to DummyClass._PyObMeta.store
        assert id(DummyClass.obs) == id(DummyClass._PyObMeta.store)

        # Assert that DummyClass.objects points to DummyClass._PyObMeta.store
        assert id(DummyClass.objects) == id(DummyClass._PyObMeta.store)
