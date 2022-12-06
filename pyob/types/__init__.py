# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ GENERAL IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from __future__ import annotations

from typing import Any, Hashable, Iterable, Mapping, Sequence, TypeVar

# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ PROJECT IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from pyob.main.classes.pyob import PyOb as PyOb  # noqa
from pyob.meta.classes.pyob_class import PyObClass as PyObClass  # noqa
from pyob.store.classes.pyob_store import PyObStore as PyObStore  # noqa
from pyob.utils.sequence import FrozenDict  # noqa


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
