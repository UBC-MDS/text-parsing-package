"""
A module that creates a bar chart from a dictionary of words and their counts.
"""

def word_chart(words: dict, display_limit: int = 10, display_order: str = "descending") -> altair.vegalite.v5.api.Chart:
    """A sorted bar chart of words and their total counts.

    This function takes in a dictionary of words and, along with their counts,
    produces a bar chart of either the most popular or least popular words.
    The user has the option of setting the number of words they would like to 
    include in the chart.

    Parameters
    ----------
    words : dict
        A dictionary of words and their counts.
    display_limit : int, default=10
        The number of words to include in the chart. If there are 
        less than 10 words present, all will be included.
    display_order : str, {"ascending", "descending"}, default="descending"
        The option to look at the most popular (descending) 
        or least (ascending) popular words.

    Returns
    -------
    altair.vegalite.v5.api.Chart
        A bar chart of most or least popular words.

    Examples
    --------
    >>> word_dict = {"apple": 12, "river": 27, "cloud": 5, "stone": 19)
    >>> word_chart(word_dict)
    >>> word_chart(word_dict, display_limit=3, display_order="ascending")
    # An altair bar chart will be displayed.
    """

    ...