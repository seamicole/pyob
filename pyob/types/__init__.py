# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ GENERAL IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from __future__ import annotations
from typing import Any, Hashable, Iterable, Mapping, Sequence, TypeVar

# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ PROJECT IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from pyob.meta.classes.pyob_class import PyObClass as PyObClass  # noqa


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ ARGS
# └─────────────────────────────────────────────────────────────────────────────────────

Args = Iterable[Any]

# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ HASHABLE SEQUENCE
# └─────────────────────────────────────────────────────────────────────────────────────

HashableSequence = Sequence[Hashable | "HashableSequence"]

# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ KWARGS
# └─────────────────────────────────────────────────────────────────────────────────────

Kwargs = Mapping[str, object]

# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ PYOB META
# └─────────────────────────────────────────────────────────────────────────────────────

PyObMeta = TypeVar("PyObMeta")
PyObMetaClass = type[PyObMeta]
