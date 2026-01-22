"""
Unit tests for the count_unique_words function in the count_unique_words module.
This test file aims to validate the output for this function given some expected 
input data and unexpected edge case input data.
"""

from text_parsing_package.count_words import count_unique_words
import pytest

def test_expected_input():
    normal_input_example_1 = 'I go where I go'
    assert count_unique_words(normal_input_example_1) == {'I': 2, 'go': 2, 'where': 1}

    normal_input_example_2 = 'the the the thing'
    assert count_unique_words(normal_input_example_2, ignore_words=['the']) == {'thing': 1}

    normal_input_example_3 = "I'll be home soon!"
    assert count_unique_words(normal_input_example_3, count_punc=True) == {
        "I'll": 1, 'be': 1, 'home': 1, 'soon': 1, '!': 1
    }

def test_whitespace_splitting_more_robust():
    # Previously: split(' ') would produce empty-string tokens for multiple spaces/newlines
    text = "I   go\nwhere\tI go"
    assert count_unique_words(text) == {'I': 2, 'go': 2, 'where': 1}

def test_case_insensitive_option():
    text = "The the THE thing"
    assert count_unique_words(text, ignore_words=['the'], case_sensitive=False) == {'thing': 1}

def test_ignore_words_accepts_other_iterables():
    text = "a a b"
    assert count_unique_words(text, ignore_words={'a'}) == {'b': 1}  # set works

def test_unexpected_input():
    # Empty string -> warning + {}
    with pytest.warns(UserWarning):
        assert count_unique_words('') == {}

    # Whitespace-only string -> warning + {}
    with pytest.warns(UserWarning):
        assert count_unique_words('   \n\t') == {}

    with pytest.raises(TypeError):
        count_unique_words(1)  # text must be str

    with pytest.raises(TypeError):
        count_unique_words('THE', ignore_words=1)  # ignore_words must be iterable of str

    with pytest.raises(TypeError):
        count_unique_words('THE', ignore_words=['the', 1])  # must contain only strings

    with pytest.raises(TypeError):
        count_unique_words('THE', count_punc=1)  # must be bool (int rejected)

    with pytest.raises(TypeError):
        count_unique_words('THE', case_sensitive=1)  # must be bool (int rejected)

def test_punctuation_only_when_counting_punc():
    text = "'!?.,:;"
    assert count_unique_words(text, count_punc=True) == {"'": 1,
        '!': 1, '?': 1, '.': 1, ',': 1, ':': 1, ';': 1
    }

def test_punctuation_removed_by_default():
    text = "hi!!! hi?"
    assert count_unique_words(text) == {'hi': 2}
