# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ GENERAL IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from pydantic import BaseModel


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ PYOB META MODEL
# └─────────────────────────────────────────────────────────────────────────────────────


class PyObMetaModel(BaseModel):
    """An Pydantic model for all PyObClass.PyObMeta definitions"""

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ RELATIVES
    # └─────────────────────────────────────────────────────────────────────────────────

    # Initialize list of parent classes to None
    Parents = None

    # Initialize list of child classes to None
    Children = None

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
