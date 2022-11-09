# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ GENERAL IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from pydantic import BaseModel
from typing import Type


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ PYOB META MODEL
# └─────────────────────────────────────────────────────────────────────────────────────


class PyObMetaModel(BaseModel):
    """An Pydantic model for all PyObClass.PyObMeta definitions"""

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ RELATIVES
    # └─────────────────────────────────────────────────────────────────────────────────

    # Initialize list of parent classes to None
    Parents: list[Type["PyOb"]] = None

    # Initialize list of child classes to None
    Children: list[Type["PyOb"]] = None

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ STORE SETTINGS
    # └─────────────────────────────────────────────────────────────────────────────────

    # Initialize keys to None
    keys: list[str] = None

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ AESTHETIC SETTINGS
    # └─────────────────────────────────────────────────────────────────────────────────

    # Initialize string field
    string: str = None

    # Initialize labels to None
    label_singular: str = None
    label_plural: str = None


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ CIRCULAR IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from pyob.main.classes.pyob import PyOb  # noqa

PyOb.update_forward_refs()
