"""
A module cleans a string of text and parses it into a list of individual words
"""

def clean_text(text, pref_case='lower', rm_all_punc=True, punctuation=None) -> list:
    """
    Split a string of text into a list of words.

    This function cleans the string of text according to the function arguments

    Parameters
    ----------
    text : str
        Any string of words, with or without punctuation.
    pref_case : str, default='lower'
        The case to convert the string to - possible values are 'upper', 
        'lower', 'asis'

    Returns
    -------
    list
        A list containing each individual word in the input text string

    Examples
    --------
    >>> 

    """
    ...