# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ GENERAL IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from hypothesis import example, given
from hypothesis.strategies import lists, sampled_from, text
from string import ascii_letters, punctuation
from typing import List

# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ PROJECT IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from pyob.tools.string import pascalize


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ TEST PASCALIZE
# └─────────────────────────────────────────────────────────────────────────────────────


@given(words=lists(text(alphabet=ascii_letters)), delimiter=sampled_from(punctuation))
@example(words=["foo", "bar"], delimiter=" ")  # "foo bar" --> "FooBar"
@example(words=["foo", "bar"], delimiter="-")  # "foo-bar" --> "FooBar"
@example(words=["foo", "bar"], delimiter="_")  # "foo_bar" --> "FooBar"
@example(words=["foo", "BAR"], delimiter="_")  # "foo_API" --> "FooBAR"
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
