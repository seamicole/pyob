# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ GENERAL IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from __future__ import annotations
from typing import Generator, TYPE_CHECKING

# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ PROJECT IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

if TYPE_CHECKING:
    from pyob.types import PyObClass


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ YIELD PARENTS
# └─────────────────────────────────────────────────────────────────────────────────────


def yield_parents(Child: PyObClass) -> Generator[PyObClass, None, None]:
    """Returns a generator of PyOb class parent PyOb classes"""

    # Get PyObMetaclass
    PyObMetaclass = type(Child)

    # Iterate over child's base classes
    for Base in Child.__bases__:

        # Yield base if it shares the child's metaclass, i.e. PyObMetaclass
        if type(Base) is PyObMetaclass:
            yield Base
