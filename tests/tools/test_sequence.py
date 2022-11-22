# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ GENERAL IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from __future__ import annotations

from hypothesis import given
from hypothesis.strategies import lists, integers, sampled_from
from typing import Sequence, Callable

# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ PROJECT IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from pyob.tools.sequence import freezeset


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ TEST FREEZESET PROPERTIES
# └─────────────────────────────────────────────────────────────────────────────────────


@given(
    sequence=lists(integers(min_value=-5, max_value=5)).filter(
        lambda x: len(x) > len(set(x))
    ),
    sequence_type=sampled_from([list, set, tuple]),
)
def test_freezeset_properties(
    sequence: Sequence[int], sequence_type: Callable[[Sequence[int]], Sequence[int]]
) -> None:
    """Tests the properties of the pyob.tools.sequence.freezeset function"""

    # Cast sequence to type
    sequence = sequence_type(sequence)

    # Convert sequence to a frozenset
    sequence_frozen = freezeset(sequence)

    # Assert that the result is a frozenset
    assert type(sequence_frozen) is frozenset

    # Assert that the frozenset is equal to the set of the sequence
    assert sequence_frozen == set(sequence)


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ TEST FREEZESET IS APPLIED RECURSIVELY
# └─────────────────────────────────────────────────────────────────────────────────────


def test_freezeset_is_applied_recursively() -> None:
    """Tests that freezeset is also applied to nested sequences"""

    # Define a level-one nested sequence
    sequence_l1 = ["a", "b", "c", "b", "a"]

    # Define a level-two nested sequence
    sequence_l2 = ["d", "e", "f", "e", "d"]

    # Define a sequence that will incorporate both of these nested sequences
    sequence = [
        "g",
        "h",
        sequence_l1,
        "i",
        "h",
        ["k", "l", sequence_l2, "m", "l", "k"],
        "g",
    ]

    # Assert that sequences on all levels are converted to a frozenset
    assert freezeset(sequence) == frozenset(
        [
            "g",
            "h",
            frozenset(sequence_l1),
            "i",
            frozenset(["k", "l", frozenset(sequence_l2), "m"]),
        ]
    )
