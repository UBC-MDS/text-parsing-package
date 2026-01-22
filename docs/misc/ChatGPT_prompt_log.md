### 524 W3 M3 ChatGPT Prompt (5.2 model, default settings)

Source: https://chatgpt.com/ - OpenAI  
 
**Prompt for count_unique_words function and tests improvements:**

--- *Start ChatGPT Prompt Input*

Improve this function specification by handling errors more efficiently or explicitly, improving functionality or options and adding corresponding simple unit tests to validate the changes. Explain each change and why it was made. Make the changes simple and easy to follow, do not rebuild the function from the ground-up.

Here is the function specification:

```python
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
```

Here is the testing file to be run with pytest:

```python
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
```

--- *End ChatGPT Prompt Input*

--- *Start ChatGPT Output*

Below is a small, incremental set of changes that keeps the function’s structure, but makes it more robust, clearer about behavior, and easier to use on “real” text. I also included simple pytest unit tests that validate each change.

Updated function (minimal refactor, better validation + options)

```python
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
```

Updated pytest file (adds tests for the new behavior)

```python
"""
Unit tests for the count_unique_words function in the count_unique_words module.
This test file aims to validate the output for this function given some expected
input data and unexpected edge case input data.
"""

from text_parsing_package.count_words import count_unique_words
import pytest

def test_expected_input():
    normal_input_example_1 = 'I go where I go'
    assert count_unique_words(normal_input_example_1) == {'I': 2, 'go': 2, 'where': 1}

    normal_input_example_2 = 'the the the thing'
    assert count_unique_words(normal_input_example_2, ignore_words=['the']) == {'thing': 1}

    normal_input_example_3 = "I'll be home soon!"
    assert count_unique_words(normal_input_example_3, count_punc=True) == {
        "I'll": 1, 'be': 1, 'home': 1, 'soon': 1, '!': 1
    }

def test_whitespace_splitting_more_robust():
    # Previously: split(' ') would produce empty-string tokens for multiple spaces/newlines
    text = "I   go\nwhere\tI go"
    assert count_unique_words(text) == {'I': 2, 'go': 2, 'where': 1}

def test_case_insensitive_option():
    text = "The the THE thing"
    assert count_unique_words(text, ignore_words=['the'], case_sensitive=False) == {'thing': 1}

def test_ignore_words_accepts_other_iterables():
    text = "a a b"
    assert count_unique_words(text, ignore_words={'a'}) == {'b': 1}  # set works

def test_unexpected_input():
    # Empty string -> warning + {}
    with pytest.warns(UserWarning):
        assert count_unique_words('') == {}

    # Whitespace-only string -> warning + {}
    with pytest.warns(UserWarning):
        assert count_unique_words('   \n\t') == {}

    with pytest.raises(TypeError):
        count_unique_words(1)  # text must be str

    with pytest.raises(TypeError):
        count_unique_words('THE', ignore_words=1)  # ignore_words must be iterable of str

    with pytest.raises(TypeError):
        count_unique_words('THE', ignore_words=['the', 1])  # must contain only strings

    with pytest.raises(TypeError):
        count_unique_words('THE', count_punc=1)  # must be bool (int rejected)

    with pytest.raises(TypeError):
        count_unique_words('THE', case_sensitive=1)  # must be bool (int rejected)

def test_punctuation_only_when_counting_punc():
    text = "!?.,:;"
    assert count_unique_words(text, count_punc=True) == {
        '!': 1, '?': 1, '.': 1, ',': 1, ':': 1, ';': 1
    }

def test_punctuation_removed_by_default():
    text = "hi!!! hi?"
    assert count_unique_words(text) == {'hi': 2}
```

What changed and why (each change is small and targeted)
1. Whitespace splitting is now correct for “real” text
    - Change: text.split(' ') → text.split()
    - Why: split() handles any whitespace (multiple spaces, tabs, newlines) and doesn’t create '' tokens. That means you no longer need to “clean up” empty keys later.
2. Empty input handling is more explicit
    - Change: if len(text) == 0 → if text.strip() == ""
    - Why: " " or "\n\t" should behave like empty text: return {} and warn.
3. ignore_words accepts any iterable of strings
    - Change: previously required list; now accepts list | set | tuple | ...
    - Why: It’s a simple usability boost. Passing a set is common and faster for membership checks.
4. ignore_words elements are validated
    - Change: if ignore_words=['the', 1], we raise TypeError
    - Why: Failing early with a clear error message prevents weird runtime behavior and makes bugs easier to spot.
5. Added case_sensitive option (default keeps current behavior)
    - Change: new parameter case_sensitive: bool = True
    - Why: Your docstring currently says “case-sensitive,” but many users want case-insensitive counts. This option adds that without changing the default behavior.
6. More predictable punctuation counting
    - Change: when count_punc=True, punctuation is spaced on both sides using r" \1 "
    - Why: This makes tokenization consistent, even when punctuation is stuck to words (e.g., "soon!").
7. More efficient ignore logic
    - Change: filter ignored words before counting instead of counting then popping.
    - Why: It’s simpler and avoids unnecessary work, especially on long texts.

If you want one more tiny improvement (still simple): add a keep_numbers: bool = True option to decide whether “2026” should be counted as a word. But the above keeps your original intent and improves robustness without rebuilding anything.

--- *End ChatGPT Output*

Explanation of Prompt Usage.

I first accepted all the ChatGPT changes to the function and test file on the isolated branch "update-count-words" and committed the changes to keep track of the diffs introduced by ChatGPT. Then I validated the changes to the function and tests by using PyTest to look at the coverage and check that all tests passed. If the function does not behave as expected and the tests do not pass, I will revert the function specification to the original and incrementally add small improvements that do not break the function.
