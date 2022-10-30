# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ HEXIFY
# └─────────────────────────────────────────────────────────────────────────────────────


def hexify(obj) -> str:
    """Returns the hex of a Python object's ID in memory"""

    # Return hex of object's ID
    return hex(id(obj))
