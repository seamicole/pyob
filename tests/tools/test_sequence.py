# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ GENERAL IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from hypothesis import given
from hypothesis.strategies import (
    booleans,
    composite,
    integers,
    lists,
    sampled_from,
    text,
)
from string import ascii_lowercase

# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ PROJECT IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from pyob.tools.sequence import deduplicate
from pyob.types import Sequence


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ SEQUENCES
# └─────────────────────────────────────────────────────────────────────────────────────


@composite
def sequences(draw, sequence_types):
    """
    Generates a non-distinct elements list, i.e. a list with with at least one repeated
    element
    """

    # Get sequence type
    sequence_type = draw(sampled_from(sequence_types))

    # Get sequence
    sequence = draw(
        lists(
            integers(min_value=-2, max_value=2)
            | text(alphabet=ascii_lowercase[:5], max_size=1)
            | booleans(),
            max_size=20,
        ).filter(lambda x: len(x) > len(set(x)))
    )

    # Return sequence
    return sequence_type(sequence)


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ TEST DEDUPLICATE PROPERTIES
# └─────────────────────────────────────────────────────────────────────────────────────


@given(sequence=sequences(sequence_types=(list, set, tuple)))
def test_deduplicate_properties(sequence: Sequence) -> None:
    """
    Tests the expected output properties of the pyob.tools.sequence.deduplicate function
    """

    # Get deduplicated sequence
    deduplicated = deduplicate(sequence, recurse=False)

    # Assert that the deduplicated sequence is of type sequence
    assert type(deduplicated) is type(sequence)

    # Assert that the length of the deduplicated sequence represents distinct elements
    assert len(deduplicated) == len(set(sequence))


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ TEST DEDUPLICATE PRESERVES ELEMENT ORDER
# └─────────────────────────────────────────────────────────────────────────────────────


@given(sequence=sequences(sequence_types=(list,)))
def test_deduplicate_preserves_element_order(sequence: Sequence):
    """
    Tests that the output of pyob.tools.sequence.deduplicate function preserves the
    original order of the input sequence
    """

    # Get deduplicated sequence
    deduplicated = deduplicate(sequence, recurse=False)

    # Initialize a seen set
    seen = set()

    # Create a reverse list of deduplicated elements
    rededuplicated = deduplicated[::-1]

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


@given(sequence=sequences(sequence_types=(list,)))
def test_deduplicate_recursion_applies_to_nested_sequences(sequence: Sequence):
    """
    Tests that the output of pyob.tools.sequence.deduplicate function preserves the
    original order of the input sequence
    """

    # Deduplicate the sequence
    deduplicated = deduplicate(sequence, recurse=False)

    # Create a new sequence with nested sequences
    sequence = [
        "a",
        "b",
        sequence,
        "a",
        ["a", "b", sequence, "a", "c"],
        "c",
    ]

    # Assert the that deduplicate is applied to nested sequences
    assert deduplicate(sequence, recurse=True) == [
        "a",
        "b",
        deduplicated,
        ["a", "b", deduplicated, "c"],
        "c",
    ]
