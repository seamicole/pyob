# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ GENERAL IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from hypothesis import example, given
from hypothesis.strategies import lists, sampled_from, text
from string import ascii_letters, ascii_lowercase, punctuation
from typing import List

# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ PROJECT IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from pyob.tools.string import pascalize, split_pascal


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ TEST PASCALIZE
# └─────────────────────────────────────────────────────────────────────────────────────


@given(words=lists(text(alphabet=ascii_letters)), delimiter=sampled_from(punctuation))
@example(words=["foo", "bar"], delimiter=" ")  # "foo bar" --> "FooBar"
@example(words=["foo", "bar"], delimiter="-")  # "foo-bar" --> "FooBar"
@example(words=["foo", "bar"], delimiter="_")  # "foo_bar" --> "FooBar"
@example(words=["foo", "BAR"], delimiter="_")  # "foo_BAR" --> "FooBAR"
def test_pascalize(words: List[str], delimiter: str) -> None:
    """Tests the expected output of the pyob.tools.string.pascalize function"""

    # Remove empty strings from words
    words = [word for word in words if word]

    # Construct string from words and delimiter
    string = delimiter.join(words)

    # Pascalize string
    pascalized = pascalize(string=string, delimiter=delimiter)

    # Assert that string is Pascalized as expected
    assert pascalized == "".join([word[0].upper() + word[1:] for word in words])


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ TEST SPLIT PASCAL
# └─────────────────────────────────────────────────────────────────────────────────────


@given(words=lists(text(alphabet=ascii_lowercase)))
@example(words=["Foo", "Bar"])  # "FooBar" --> ["Foo", "Bar"]
def test_split_pascal(words: List[str]) -> None:
    """Tests the expected output of the pyob.tools.string.split_pascal function"""

    # Remove empty strings from words
    words = [word for word in words if word]

    # Ensure that the first letter of every word is capitalized
    words = [word[0].upper() + word[1:] for word in words]

    # Construct Pascalized string from words
    string = "".join(words)

    # Split string by Pascal case
    string_split = split_pascal(string=string)

    # Initialize expected result
    expected = []

    # Iterate over words
    for word in words:

        # Check if length of word is 1 and there is a previous word
        if len(word) == 1 and expected:

            # Get previous word
            word_previous = expected[-1]

            # Check if previous word is uppercase
            if word_previous.isupper():

                # Append word to existing word
                expected.append(expected.pop() + word)
                continue

        # Append word to expected
        expected.append(word)

    # Assert that split string matches the expected result
    assert string_split == expected
