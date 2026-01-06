
def count_unique_words(text: str) -> dict:
    """
    Count the instances of unique words in a text string.

    Input text is assumed to be separated by single spaces and punctuation
    has been removed. Additional pre-processing is required for correct word
    parsing and counting if the input text words are not separated by single
    spaces and/or the text contains punctuation.

    Parameters
    ----------
    text : str
        string of text to count instances of case sensitive unique words
    
    Returns
    -------
    word_count_dict: dict
        A dictionary of words as str keys and their counts as int values

    Raises
    ------
    TypeError
        If input type is incorrect.
    
    """

    ...