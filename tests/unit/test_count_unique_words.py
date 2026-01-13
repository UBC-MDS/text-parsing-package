"""
Unit tests for the count_unique_words function in the count_words module.
This test file aims to validate the output for this function given some 
expected input data and unexpected edge case input data.
"""

import os
import sys
from collections import Counter

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.text_parsing_package.count_words import count_unique_words

def test_normal_input():
    """
    Test count_unique_words with a simple expected input.
    """
    
    normal_input_example = 'I go where I go'
    assert count_unique_words() == {'I': 2, 'go': 1, 'where': 1}