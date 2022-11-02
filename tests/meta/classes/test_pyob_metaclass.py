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
