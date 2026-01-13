"""
A module containing the count_unique_words function for general use or in
conjunction with other modules in the text parsing package. This module aids
in numerically analyzing the frequency of unique words in a section of text.
"""

# Import Counter, re and warnings from base python package
from collections import Counter
import warnings
import re

def count_unique_words(text: str, ignore_words: list[str] = None, count_punc: bool = False) -> dict[str, int]:
    """
    Count the instances of unique, case-sensitive words in a text string.

    Input text is assumed to be separated by single spaces and punctuation
    has been removed. Additional pre-processing is required for correct word
    parsing and counting if the input text words are not separated by single
    spaces and/or the text contains punctuation.

    Parameters
    ----------
    text : str
        string of text to count instances of case sensitive unique words.
    
    ignore_words: list[str], default=None
        list of strings of words to exclude from the counting, by default all unique words are included.

    count_punc: bool, default=False
        option to count the instances of unique punctuation in the input text string if set to True,
        otherwise all punctuation is removed by default.
        
    Returns
    -------
    word_count_dict: dict
        A dictionary of words as str keys and their counts as int values

    Raises
    ------
    TypeError
        If input type is incorrect.

    Examples
    --------
    word_count_dict = count_unique_words('I go where I go')
    >>> {'I': 2, 'go': 2, where: 1}

    word_count_dict = count_unique_words('The the the thing', ignore_words = ['the'])
    >>> {'thing': 1}

    """

    # Check the input type for the text parameter is a string
    if not isinstance(text, str):
        raise TypeError(f'"text" parameter must be a str, not a {type(text)}.')
    
    # Check the input type for the ignore_words parameter is a list[str] or None
    if ignore_words is not None and not isinstance(ignore_words, list):
        raise TypeError(f'"ignore_words" parameter must be a list[str] | None, not a {type(ignore_words)}.')
    
    # Check the input type for the count_punc parameter is a string
    if not isinstance(count_punc, bool):
        raise TypeError(f'"count_punc" parameter must be a bool, not a {type(count_punc)}.')

    # If the passed string is empty return and empty dict and warn the user
    if len(text)==0:
        word_count_dict = {}
        warnings.warn(f'You passed "{text}" as a string, returning an empty word_count_dict.')
        return word_count_dict
    
    # Remove punctuation unless user explicitly wants unique punctuation instances to be counted
    if not count_punc:
        # Remove all punctuation if the default value for count_punc is used
        text = re.sub(r"[^\w\s']", '', text)
    else:
        # Extra spaces added to any matched punctuation to be counted for the split below
        text = re.sub(r"[^\w\s']", r' \g<0>', text)
    
    # assume a new word occurs on a space, if not use the clean_text function first
    words_list = text.split(' ')

    # built-in function to count repeated strings in a list this instead of building 
    # from scratch which may result in have bad time complexity
    word_count_dict = dict(Counter(words_list))

    # If ignore_words is passed as non-empty list[str], remove these keys from the dict
    if ignore_words!=None and len(ignore_words)>0:
        for word in ignore_words:
            word_count_dict.pop(word, None)
    
    # Remove any empty space keys if they exist from punctuation counting
    word_count_dict.pop('', None)

    return word_count_dict
