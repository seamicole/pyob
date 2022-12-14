# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ GENERAL IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from __future__ import annotations

from typing import Any, Hashable, Iterable, Mapping, Sequence

# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ PROJECT IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from pyob.main.classes.pyob import PyOb as PyOb
from pyob.meta.classes.pyob_class import PyObClass as PyObClass  # noqa
from pyob.store.classes.pyob_store import PyObStore as PyObStore  # noqa
from pyob.utils.classes.sequence import FrozenDict as FrozenDict  # noqa


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
