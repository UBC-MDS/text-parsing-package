"""
Unit tests for the count_unique_words function in the count_unique_words module.
This test file aims to validate the output for this function given some expected 
input data and unexpected edge case input data.
"""

# Import the count_unique_words function from the count_words module in the package
from text_parsing_package.count_words import count_unique_words
import pytest

def test_expected_input():
    """
    Test count_unique_words with a simple expected inputs.
    """

    normal_input_example_1 = 'I go where I go'
    assert count_unique_words(normal_input_example_1) == {'I': 2, 'go': 2, 'where': 1}

    normal_input_example_2 = 'the the the thing'
    assert count_unique_words(normal_input_example_2, ignore_words=['the']) == {'thing': 1}

    normal_input_example_3 = "I'll be home soon!"
    assert count_unique_words(normal_input_example_3, count_punc=True) == {"I'll": 1, 'be': 1, 'home': 1, 'soon': 1, '!': 1}

def test_unexpected_input():
    """
    Test count_unique_words with a simple unexpected inputs.
    """

    # This should raise a warning to the user that an empty dict is returned
    with pytest.warns(UserWarning):
        abnormal_input_example_1 = ''
        assert count_unique_words(abnormal_input_example_1) == {}

    with pytest.raises(TypeError):
        abnormal_input_example_2 = 1
        count_unique_words(abnormal_input_example_2)

    with pytest.raises(TypeError):
        abnormal_input_example_3 = 'THE'
        count_unique_words(abnormal_input_example_3, ignore_words=1)
    
    with pytest.raises(TypeError):
        abnormal_input_example_3 = 'THE'
        count_unique_words(abnormal_input_example_3, count_punc=1)
    
    abnormal_input_example_4 = "!?.,:;"
    assert count_unique_words(abnormal_input_example_4, count_punc=True) == {'!':1, '?':1, '.':1, ',':1, ':':1, ';':1}