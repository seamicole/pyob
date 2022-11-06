# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ PROJECT IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from pyob import PyOb


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ TEST PYOB METACLASS
# └─────────────────────────────────────────────────────────────────────────────────────


class TestPyObMetaclass:
    """A test class for PyObMetaclass"""

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ TEST INIT CLONES PYOB META
    # └─────────────────────────────────────────────────────────────────────────────────

    def test_init_clones_pyob_meta(self):
        """Tests that the definition of a new PyOb class always clones a PyObStore"""

        # Define a parent PyObClass
        class PyObClassParent(PyOb):
            """A dummy PyOb class"""

            class PyObMeta:
                """PyObMeta Class"""

        # Define a child PyObClass
        class PyObClassChild1(PyOb):
            """A dummy PyOb class"""

        # Assert that even inherited PyObMeta classes (no PyObMeta defined on child)
        # are given their own PyObMeta object in memory
        assert id(PyObClassChild1.PyObMeta) != id(PyObClassParent.PyObMeta)

        # Define a child PyObClass
        class PyObClassChild2(PyOb):
            """A dummy PyOb class"""

            class PyObMeta:
                """PyObMeta Class"""

        # Assert that uninherited PyObMeta classes (explicit PyObMeta defined on child)
        # are also given their own PyObMeta object in memory
        assert id(PyObClassChild2.PyObMeta) != id(PyObClassParent.PyObMeta)

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ TEST INIT CREATES STORE
    # └─────────────────────────────────────────────────────────────────────────────────

    def test_init_creates_store(self):
        """Tests that the definition of a new PyOb class always creates a new store"""

        # Define a parent PyObClass
        class PyObClassParent(PyOb):
            """A dummy PyOb class"""

            class PyObMeta:
                """PyObMeta Class"""

        # Define a child PyObClass
        class PyObClassChild1(PyOb):
            """A dummy PyOb class"""

        # Assert that even inherited PyObMeta classes (no PyObMeta defined on child)
        # are given their own PyObMeta store objects in memory
        assert id(PyObClassChild1.PyObMeta.store) != id(PyObClassParent.PyObMeta.store)

        # Define a child PyObClass
        class PyObClassChild2(PyOb):
            """A dummy PyOb class"""

            class PyObMeta:
                """PyObMeta Class"""

        # Assert that uninherited PyObMeta classes (explicit PyObMeta defined on child)
        # are also given their own PyObMeta store objects in memory
        assert id(PyObClassChild2.PyObMeta.store) != id(PyObClassParent.PyObMeta.store)

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ TEST INIT ASSIGNS PARENTS
    # └─────────────────────────────────────────────────────────────────────────────────

    def test_init_assigns_parents(self):
        """Tests that parents of a PyOb class are assigned in its PyObMeta"""

        # Define a parent PyObClass
        class PyObClassParent1(PyOb):
            """A dummy PyOb class"""

        # Assert that the parent class only has one parent (PyOb)
        assert len(PyObClassParent1.PyObMeta.Parents) == 1

        # Assert that the only parent of the parent class is PyOb
        assert PyObClassParent1.PyObMeta.Parents[0] is PyOb

        # Define another parent PyObClass
        class PyObClassParent2(PyOb):
            """A dummy PyOb class"""

        # Define a child PyObClass
        class PyObClassChild(PyObClassParent1, PyObClassParent2):
            """A dummy PyOb class"""

        # Assert that the child class has two parents
        assert len(PyObClassChild.PyObMeta.Parents) == 2

        # Assert that the parents of the child class are the two inherited parents
        assert PyObClassChild.PyObMeta.Parents[0] is PyObClassParent1
        assert PyObClassChild.PyObMeta.Parents[1] is PyObClassParent2

        # Get list of all parent lists
        parent_lists = [
            PyObClass.PyObMeta.Parents
            for PyObClass in (PyObClassParent1, PyObClassParent2, PyObClassChild)
        ]

        # Convert parents lists to a list of IDs
        parent_lists = [id(parent_list) for parent_list in parent_lists]

        # Assert that all these lists are distinct
        # i.e. No two PyObClasses share a parents list
        assert len(set(parent_lists)) == len(parent_lists)

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ TEST INIT ASSIGNS CHILDREN
    # └─────────────────────────────────────────────────────────────────────────────────

    def test_init_assigns_children(self):
        """Tests that children of a PyOb class are assigned in its parent PyObMetas"""

        # Define a parent PyObClass
        class PyObClassParent1(PyOb):
            """A dummy PyOb class"""

        # Assert that the parent class is a child of PyOb
        assert PyObClassParent1 in PyOb.PyObMeta.Children

        # Assert that the parent class currently has no children
        assert len(PyObClassParent1.PyObMeta.Children) == 0

        # Define another parent PyObClass
        class PyObClassParent2(PyOb):
            """A dummy PyOb class"""

        # Define a child PyObClass
        class PyObClassChild1(PyObClassParent1, PyObClassParent2):
            """A dummy PyOb class"""

        # Iterate over parent classes
        for PyObClassParent in (PyObClassParent1, PyObClassParent2):

            # Assert that the parent class now has one child
            assert len(PyObClassParent.PyObMeta.Children) == 1

            # Assert that the child class is the first child class
            assert PyObClassParent.PyObMeta.Children[0] is PyObClassChild1

        # Define another child PyObClass
        class PyObClassChild2(PyObClassParent2):
            """A dummy PyOb class"""

        # Assert that the first parent class still has only one child
        assert len(PyObClassParent1.PyObMeta.Children) == 1

        # Assert that the second parent class now has two children
        assert len(PyObClassParent2.PyObMeta.Children) == 2

        # Assert that the second child was added to the second parent's children
        assert PyObClassParent2.PyObMeta.Children[1] is PyObClassChild2

        # Get list of all child lists
        child_lists = [
            PyObClass.PyObMeta.Children
            for PyObClass in (
                PyObClassParent1,
                PyObClassParent2,
                PyObClassChild1,
                PyObClassChild2,
            )
        ]

        # Convert child lists to a list of IDs
        child_lists = [id(child_list) for child_list in child_lists]

        # Assert that all these lists are distinct
        # i.e. No two PyObClasses share a childs list
        assert len(set(child_lists)) == len(child_lists)

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ TEST INIT LABELS DO NOT INHERIT
    # └─────────────────────────────────────────────────────────────────────────────────

    def test_init_labels_do_not_inherit(self):
        """Tests to ensure that labels do not inherit from parent PyObMeta classes"""

        # Define a parent PyObClass
        class PyObClassParent(PyOb):
            """A dummy PyOb class"""

            class PyObMeta:
                """PyObMeta Class"""

                label_singular = "Parent"
                label_plural = "Parents"

        # Assert that the parent labels are preserved
        assert PyObClassParent.PyObMeta.label_singular == "Parent"
        assert PyObClassParent.PyObMeta.label_plural == "Parents"

        # Define a child PyObClass that defines its own labels
        class PyObClassChild1(PyObClassParent):
            """A dummy PyOb class"""

            class PyObMeta:
                """PyObMeta Class"""

                label_singular = "Kid"
                label_plural = "Kids"

        # Assert that the child labels are preserved
        assert PyObClassChild1.PyObMeta.label_singular == "Kid"
        assert PyObClassChild1.PyObMeta.label_plural == "Kids"

        # Define another child PyObClass that defines as PyObMeta but not labels
        class PyObClassChild2(PyObClassParent):
            """A dummy PyOb class"""

            class PyObMeta:
                """PyObMeta Class"""

        # Assert that the child labels are derived from the class name
        assert PyObClassChild2.PyObMeta.label_singular == "Py Ob Class Child2"
        assert PyObClassChild2.PyObMeta.label_plural == "Py Ob Class Child2s"

        # Define another child PyObClass that defines no PyObMeta
        class PyObClassChild3(PyObClassParent):
            """A dummy PyOb class"""

        # Assert that the child labels are still derived from the class name
        assert PyObClassChild3.PyObMeta.label_singular == "Py Ob Class Child3"
        assert PyObClassChild3.PyObMeta.label_plural == "Py Ob Class Child3s"

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ TEST INIT LABEL ASSIGNMENT
    # └─────────────────────────────────────────────────────────────────────────────────

    def test_init_label_assignment(self):
        """Tests that the init method assigns PyObMeta labels as expected"""

        # Define a dummy PyObClass
        class Nation(PyOb):
            """A dummy PyOb class"""

            class PyObMeta:
                """PyObMeta Class"""

                label_singular = "Country"
                label_plural = "Countries"

        # Assert that PyObMeta labels are retained
        assert Nation.PyObMeta.label_singular == "Country"
        assert Nation.PyObMeta.label_plural == "Countries"

        # Define a dummy PyObClass
        class Nation(PyOb):
            """A dummy PyOb class"""

        # Assert that PyObMeta labels are generated according to class name
        assert Nation.PyObMeta.label_singular == "Nation"
        assert Nation.PyObMeta.label_plural == "Nations"

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ TEST INIT LABEL PLURALIZATION
    # └─────────────────────────────────────────────────────────────────────────────────

    def test_init_label_pluralization(self):
        """Tests that generated PyObMeta labels use the correct plural inflections"""

        # Define a dummy PyObClass
        class Ant(PyOb):
            """A dummy PyOb class"""

        # Assert that PyObMeta labels are generated according to class name
        assert Ant.PyObMeta.label_singular == "Ant"
        assert Ant.PyObMeta.label_plural == "Ants"

        # Define a dummy PyObClass
        class Box(PyOb):
            """A dummy PyOb class"""

        # Assert that PyObMeta labels are generated according to class name
        assert Box.PyObMeta.label_singular == "Box"
        assert Box.PyObMeta.label_plural == "Boxes"

        # Define a dummy PyObClass
        class City(PyOb):
            """A dummy PyOb class"""

        # Assert that PyObMeta labels are generated according to class name
        assert City.PyObMeta.label_singular == "City"
        assert City.PyObMeta.label_plural == "Cities"

        # Define a dummy PyObClass
        class Ditch(PyOb):
            """A dummy PyOb class"""

        # Assert that PyObMeta labels are generated according to class name
        assert Ditch.PyObMeta.label_singular == "Ditch"
        assert Ditch.PyObMeta.label_plural == "Ditches"
