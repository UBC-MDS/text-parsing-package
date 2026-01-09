"""
A module cleans a string of text and parses it into a list of individual words
"""

def clean_text(text: str, pref_case: str = "lower", rm_all_punc: bool = True, punctuation: list = None) -> list:
    """
    Cleans a string of text according to function arguments.

    Parameters
    ----------
    text : str
        Any string of words, with or without punctuation.
    pref_case : str, {"lower", "upper", "asis"}, default="lower"
        The case to convert the string to. "asis" indicates that the type case should not be changed
    rm_all_punc : bool, default=True
        Indicates whether ALL punctuation should be removed from the string
    punctuation : list or None, default=None
        Only used if rm_all_punc is false, punctuation should be a list of specific punctuation to remove, all other punctuation will remain in the clean text string.
        
    Returns
    -------
    string
       A cleaned string without whitespace other than spaces, coverted to a specific case if relevant and with punctuation removed as specified

    Examples
    --------
    >>> clean_text("Hello, it is so lovely to meet you today.")
    "hello it is so lovely to meet you today"

    >>> clean_text("Hello, it is so lovely to meet you today.", pref_case="upper", rm_all_punc=False, punctuation=[",", "!"])
    "HELLO IT IS SO LOVELY TO MEET YOU TODAY."

    """
    ...