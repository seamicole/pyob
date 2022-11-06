# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ GENERAL IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

import inflect

from typing import Type, TYPE_CHECKING

# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ PROJECT IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from pyob.tools.string import split_pascal

if TYPE_CHECKING:
    import pyob.main.classes.PyOb


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ CREATE LABEL SINGULAR
# └─────────────────────────────────────────────────────────────────────────────────────


def create_label_singular(PyObClass: Type["pyob.main.classes.PyOb"]) -> str:
    """Creates a singular label for a PyOb class"""

    # Create singular label as a derivative of PyObClass.__name__
    label_singular = " ".join(split_pascal(PyObClass.__name__))

    # Strip singular label
    label_singular = label_singular.strip()

    # Return singular label
    return label_singular


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ CREATE LABEL PLURAL
# └─────────────────────────────────────────────────────────────────────────────────────


def create_label_plural(PyObClass: Type["pyob.main.classes.PyOb"]) -> str:
    """Creates a plural label for a PyOb class"""

    # Initialize inflector
    inflector = inflect.engine()

    # Disable default handling of proper nouns
    # Otherwise e.g. Country will pluralize to Countrys instead of Countries
    inflector.classical(names=0)

    # Pluralize the singular label of the PyOb class
    label_plural = inflector.plural(PyObClass.PyObMeta.label_singular)

    # Return plural label
    return label_plural
