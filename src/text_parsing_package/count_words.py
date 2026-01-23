"""
A module containing the count_unique_words function for general use or in
conjunction with other modules in the text parsing package. This module aids
in numerically analyzing the frequency of unique words in a section of text.
"""

from collections import Counter
import warnings
import re
from typing import Iterable, Optional

def count_unique_words(
    text: str,
    ignore_words: Optional[Iterable[str]] = None,
    count_punc: bool = False,
    case_sensitive: bool = True,
) -> dict[str, int]:
    """
    Count the instances of unique words in a text string.

    By default, punctuation is removed (except apostrophes inside words).
    Words are split on any whitespace (spaces/tabs/newlines), not just single spaces.

    Parameters
    ----------
    text : str
        String of text to count instances of unique words.

    ignore_words : Iterable[str] | None, default=None
        Words to exclude from counting. Accepts any iterable of strings (e.g., list, set, tuple).
        Matching respects `case_sensitive`.

    count_punc : bool, default=False
        If True, punctuation symbols are tokenized and counted as separate tokens.
        If False, punctuation is removed (apostrophes inside words are kept).

    case_sensitive : bool, default=True
        If False, words are normalized to lowercase before counting (and ignore_words is too).

    Returns
    -------
    dict[str, int]
        Dictionary of tokens to counts.

    Raises
    ------
    TypeError
        If input types are incorrect or ignore_words contains non-strings.

    Examples
    --------
    count_unique_words('I go where I go')
    {'I': 2, 'go': 2, 'where': 1}

    count_unique_words('The the the thing', ignore_words=['the'], case_sensitive=False)
    {'thing': 1}
    """

    # Validate types
    if not isinstance(text, str):
        raise TypeError(f'"text" parameter must be a str, not a {type(text)}.')

    if not isinstance(count_punc, bool):
        raise TypeError(f'"count_punc" parameter must be a bool, not a {type(count_punc)}.')

    if not isinstance(case_sensitive, bool):
        raise TypeError(f'"case_sensitive" parameter must be a bool, not a {type(case_sensitive)}.')

    if ignore_words is not None:
        # Allow any iterable of strings (list/set/tuple/etc.), but reject non-iterables like int
        if isinstance(ignore_words, (str, bytes)) or not isinstance(ignore_words, Iterable):
            raise TypeError(f'"ignore_words" parameter must be an iterable of str | None, not a {type(ignore_words)}.')
        for w in ignore_words:
            if not isinstance(w, str):
                raise TypeError('"ignore_words" must contain only strings.')

    # Treat empty OR whitespace-only as empty input
    if text.strip() == "":
        warnings.warn('You passed an empty/whitespace-only string; returning an empty dict.')
        return {}

    # Normalize case if requested
    if not case_sensitive:
        text = text.lower()

    # Tokenize punctuation if requested; otherwise remove punctuation
    if count_punc:
        # Put spaces around punctuation so it becomes its own token
        # Keep apostrophes as part of words (e.g., "I'll")
        text = re.sub(r"([^\w\s'])", r" \1 ", text)
    else:
        # Remove punctuation, but keep apostrophes (inside contractions/possessives)
        text = re.sub(r"[^\w\s']", "", text)

    # Split on any whitespace (handles multiple spaces, tabs, newlines) and avoids '' tokens
    words_list = text.split()

    # Normalize ignore list to a set for efficient filtering
    ignore_set: set[str] = set()
    if ignore_words:
        ignore_set = {w if case_sensitive else w.lower() for w in ignore_words}

    # Filter ignored words before counting (avoids counting then popping)
    filtered = (w for w in words_list if w and w not in ignore_set)

    return dict(Counter(filtered))
