"""
This test module contains tests for the clean_text function
"""

import pytest
from text_parsing_package.clean_text import clean_text


good_string = "Hello, it is so lovely to meet you today."

def test_clean_text_function_args():
    """
    Tests various function arguments using the same "nice" test string
    """

    actual = clean_text(good_string)
    expected = "hello it is so lovely to meet you today"
    assert actual == expected

    actual = clean_text(good_string, pref_case="upper")
    expected = "HELLO IT IS SO LOVELY TO MEET YOU TODAY"
    assert actual == expected

    actual = clean_text(good_string, pref_case="asis")
    expected = "Hello it is so lovely to meet you today"
    assert actual == expected

    actual = clean_text(good_string, rm_all_punc=False)
    expected = "hello, it is so lovely to meet you today."
    assert actual == expected

    actual = clean_text(good_string, rm_all_punc=False, punctuation=[",", "!"])
    expected = "hello it is so lovely to meet you today."
    assert actual == expected

str_with_other_whitespace = "Hello  nice to meet     you"

def test_clean_text_whitespace():
    """
    Tests that other whitespace characters are replaced by spaces
    """
    actual = clean_text(str_with_other_whitespace)
    expected = "hello it is so lovely to meet you today"
    assert actual == expected

def test_clean_text_wrong_input():
    """
    Tests exception handling for invalid inputs
    """

    with pytest.raises(TypeError):
        clean_text(123)
    
    with pytest.raises(ValueError):
        clean_text(good_string, pref_case="capitalize")