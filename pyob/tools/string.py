# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ PASCALIZE
# └─────────────────────────────────────────────────────────────────────────────────────


def pascalize(string: str, delimiter: str = " ") -> str:
    """Converts a string to Pascal case based on a delimiter"""

    # Split string by delimiter
    string = [s.strip() for s in string.split(delimiter)]

    # Capitalize each word in split string
    string = [s[0].upper() + s[1:] for s in string if s]

    # Join string
    string = "".join(string)

    # Return string
    return string
