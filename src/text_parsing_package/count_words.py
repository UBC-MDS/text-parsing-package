"""
A module containing the count_unique_words function for general use or in
conjunction with other modules in the text parsing package. This module aids
in numerically analyzing the frequency of unique words in a section of text.
"""

def count_unique_words(text: str, ignore_words: list[str] = None) -> dict:
    """
    Count the instances of unique words in a text string.

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

    ...
