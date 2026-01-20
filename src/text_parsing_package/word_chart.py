import altair as alt
import pandas as pd

"""
A module that creates a bar chart from a dictionary of words and their counts.
"""

def word_chart(words: dict, display_limit: int = 10, display_order: str = "descending"): #-> alt.vegalite.v5.api.Chart:
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

    Raises
    ------
    TypeError
        If the parameter(s) are not of the correct type.
    ValueError
        If 'display_order' parameter is a valid option.
        
    Examples
    --------
    >>> word_dict = {"apple": 12, "river": 27, "cloud": 5, "stone": 19}
    >>> word_chart(word_dict)
    >>> word_chart(word_dict, display_limit=3, display_order="ascending")
    # An altair bar chart will be displayed.
    """

    if not isinstance(words, dict):
        raise TypeError(f"The 'words' parameter is not of type 'dict'. It is of type {type(words)}.")

    if not isinstance(display_limit, int):
        raise TypeError(f"The 'display_limit' parameter is not of type 'int'. It is of type {type(display_limit)}.")

    if not isinstance(display_order, str):
        raise TypeError(f"The 'display_order' parameter is not of type 'str'. It is of type {type(display_order)}.")

    if  display_order not in ["ascending", "descending"]:
        raise ValueError(f"The 'display_order must either be 'ascending' or 'descending'. It is {display_order}.")
    
    words = (
        pd.DataFrame.from_dict(
            words,
            orient="index",
            columns=["count"]
        ).reset_index(names="word")
    )
    
    if display_order == "ascending":
        display_title=f"The {min(display_limit, len(words))} Least Popular Words"
    else:
        display_title=f"The {min(display_limit, len(words))} Most Popular Words"

    chart = (
        alt.Chart(words).mark_bar().encode(
            alt.X("count", title="Word Count"),
            alt.Y("word", title=None, sort="-x")
        ).transform_window(
            rank="rank(count)",
            sort=[alt.SortField("count", order=display_order)]
        ).transform_filter(
            (alt.datum.rank <= display_limit)
        ).properties(
            title=display_title
        )
    )
    return chart