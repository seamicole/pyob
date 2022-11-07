# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ GENERAL IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from hypothesis import example, given
from hypothesis.strategies import integers, lists, sampled_from, text
from typing import Type

# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ PROJECT IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from pyob.tools.sequence import deduplicate
from pyob.types import Sequence


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ TEST DEDUPLICATE
# └─────────────────────────────────────────────────────────────────────────────────────


@given(
    sequence=lists(
        text(alphabet=["a", "b", "c", "d", "e"], max_size=1)
        | integers(min_value=-5, max_value=5),
        min_size=20,
    ),
    sequence_type=sampled_from([list, set, tuple]),
)
@example(sequence=[0, "", False, 0, "", False], sequence_type=tuple)
def test_deduplicate(sequence: Sequence, sequence_type: Type[Sequence]) -> None:
    """Tests the expected output of the pyob.tools.sequence.deduplicate function"""

    # Get deduplicated sequence
    deduplicated = deduplicate(sequence_type(sequence), recurse=False)

    # Assert that the deduplicated sequence is of type sequence type
    assert type(deduplicated) is sequence_type

    # Get distinct count of elements
    distinct_count = len(set(sequence))

    # Assert that the length of the deduplicated sequence represents distinct elements
    assert len(deduplicated) == distinct_count

    # Return if sequence type is set
    if sequence_type is set:
        return

    # Initialize a seen set
    seen = set()

    # Create a reverse list of deduplicated elements
    rededuplicated = list(deduplicated)[::-1]

    # Iterate over sequence
    for element in sequence:

        # Continue if element has been seen
        if element in seen:
            continue

        # Assert that element is the next item in deduplicated
        # i.e. That deduplicated preserves its original order
        assert element == rededuplicated.pop()

        # Add element to seen
        seen.add(element)

    # Create a new nested sequence
    sequence_nested = sequence_type(
        [
            "a",
            "b",
            sequence_type(sequence),
            "a",
            sequence_type(["a", "b", sequence_type(sequence), "a", "c"]),
            "c",
        ]
    )

    # Deduplicate the nested sequence
    deduplicated_nested = deduplicate(sequence_nested, recurse=True)

    # Assert that the recursive functionality works as expected
    assert deduplicated_nested == sequence_type(
        [
            "a",
            "b",
            deduplicated,
            sequence_type(["a", "b", deduplicated, "c"]),
            "c",
        ]
    )
