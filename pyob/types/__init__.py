# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ GENERAL IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from typing import Any, Iterable, Mapping

# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ PROJECT IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from pyob.meta.classes.pyob_class import PyObClass as PyObClass  # noqa


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ ANY CLASS
# └─────────────────────────────────────────────────────────────────────────────────────

AnyClass = type[type]

# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ ARGS
# └─────────────────────────────────────────────────────────────────────────────────────

Args = Iterable[Any]

# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ KWARGS
# └─────────────────────────────────────────────────────────────────────────────────────

Kwargs = Mapping[str, object]
