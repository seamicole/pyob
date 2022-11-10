# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ GENERAL IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from __future__ import annotations
from typing import TYPE_CHECKING

# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ PROJECT IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

if TYPE_CHECKING:
    from pyob.types import PyObClass


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ PYOB META BASE
# └─────────────────────────────────────────────────────────────────────────────────────


class PyObMetaBase:
    """An abstract blueprint for all PyObClass.PyObMeta definitions"""

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ RELATIVES
    # └─────────────────────────────────────────────────────────────────────────────────

    # Initialize list of parent classes to None
    Parents: list[PyObClass] | None = None

    # Initialize list of child classes to None
    Children: list[PyObClass] | None = None
