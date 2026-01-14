"""
A module cleans a string of text and parses it into a list of individual words
"""
import re

def clean_text(text: str, pref_case: str = "lower", rm_all_punc: bool = True, punctuation: list = []) -> str:
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
    punctuation : list, default=[]
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
    
    if not isinstance(text, str):
        raise TypeError(f"Expected the test input to be of type str, got {type(text)}")

    # replace non-space whitespaces in text
    text = re.sub(r'[^\S ]', ' ', text)

    # case conversion
    if pref_case == "lower":
        text = text.lower()
    elif pref_case == "upper":
        text = text.upper()
    elif pref_case == "asis":
        pass
    else:
        raise ValueError(f"Expected pref_case value in ('lower', 'upper', 'asis'), got '{pref_case}'")
    
    # punctuation
    if rm_all_punc:
        text = re.sub(r'[^\w\s]', '', text)
    else:
        for punct in punctuation:
            text = text.replace(punct, '')
    
    return text