import enchant
import pytest

from ibex_developers_manual.sort_word_list import read_word_list, sort_words


@pytest.fixture
def words() -> list[str]:
    return read_word_list()


@pytest.fixture
def dictionary() -> enchant.Dict:
    return enchant.Dict("en_GB")


def test_wordlist_is_sorted(words):
    sorted_words = sort_words(words)

    assert words == sorted_words, "word list is not sorted, run sort_word_list to sort them."


def test_wordlist_doesnt_have_duplicates_with_initial_caps(words):
    failures = []
    for word in words:
        if word.islower() and (word[0].upper() + word[1:]) in words:
            failures.append(word)

    assert failures == [], (
        "Lowercase words duplicated with an initial upper-case letter in word list, this is unnecessary. "
        "If it is a proper noun, remove the lowercase variant from the word list, otherwise remove the uppercase variant."
    )


def test_wordlist_doesnt_allow_words_that_should_be_proper_nouns(words, dictionary):
    exemptions = {
        "arg",  # Short for 'argument' - not https://en.wikipedia.org/wiki/Arg,_Kabul
        "boolean",  # Historic exemption - should be capitalised consistently & removed here
        "ethernet",  # Historic exemption - should be capitalised consistently & removed here
        "isis",  # Pragmatic exemption
        "jenkins",  # Historic exemption - should be capitalised consistently & removed here
        "linux",  # Historic exemption - should be capitalised consistently & removed here
        "md",  # Short for 'markdown', not https://en.wikipedia.org/wiki/Doctor_of_Medicine
        "nd",  # e.g. 2nd October - not Neodymium
        "synoptics",  # Neither https://en.wikipedia.org/wiki/Synoptic_Gospels nor https://en.wikipedia.org/wiki/SynOptics
        "th",  # e.g. 19th October - not Thorium
    }

    failures = []
    for word in words:
        if (
            word not in exemptions
            and word.islower()
            and not dictionary.check(word)
            and dictionary.check(word[0].upper() + word[1:])
        ):
            failures.append(word)

    assert failures == [], (
        "A word which should always have an initial capital letter was detected in lowercase in the word list. "
        "If you are certain that the lowercase variant is the correct capitalisation in our context, add it to the "
        "list of exemptions (with justification) in this test."
    )
