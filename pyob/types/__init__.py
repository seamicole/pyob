# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ GENERAL IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from typing import Any, Iterable, Mapping, TypeVar

# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ PROJECT IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from pyob.meta.classes.pyob_class import PyObClass as PyObClass  # noqa


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ ARGS
# └─────────────────────────────────────────────────────────────────────────────────────

Args = Iterable[Any]

# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ KWARGS
# └─────────────────────────────────────────────────────────────────────────────────────

Kwargs = Mapping[str, object]

# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ PYOB CHILDREN
# └─────────────────────────────────────────────────────────────────────────────────────

PyObChildren = list[PyObClass]

# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ PYOB META
# └─────────────────────────────────────────────────────────────────────────────────────

PyObMeta = TypeVar("PyObMeta")
PyObMetaClass = type[PyObMeta]

# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ PYOB PARENTS
# └─────────────────────────────────────────────────────────────────────────────────────

PyObParents = list[PyObClass]
