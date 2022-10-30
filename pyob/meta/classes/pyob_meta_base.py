# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ PYOB META BASE
# └─────────────────────────────────────────────────────────────────────────────────────


class PyObMetaBase:
    """An attribute blueprint for all PyObClass.PyObMeta definitions"""

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
    keys = None

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ AESTHETIC SETTINGS
    # └─────────────────────────────────────────────────────────────────────────────────

    # Initialize string field
    string = None

    # Initialize labels to None
    label_singular = label_plural = None
