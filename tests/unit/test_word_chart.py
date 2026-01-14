import altair as alt
import pandas as pd
import pytest

from text_parsing_package.word_chart import word_chart

test_words = {
    "apple": 12,
    "river": 27,
    "cloud": 5,
    "stone": 19,
    "forest": 8,
    "ocean": 30,
    "flame": 14,
    "shadow": 2,
    "breeze": 21,
    "mountain": 16,
    "star": 9,
    "field": 0,
    "echo": 25,
    "rain": 11,
    "sun": 29,
    "path": 6,
    "leaf": 18,
    "snow": 3,
    "wind": 24,
    "earth": 7
}

base_case = word_chart(test_words)

# test parameters

def test_invalid_words_parameter():
    """Test that a TypeError is raised when the 'words' paramenter 
    is not of type 'dict'."""
    with pytest.raises(TypeError, match="'words' parameter is not of type 'dict'"):
        word_chart(123)
        word_chart("words")

def test_invalid_display_limit_parameter():
    """Test that a TypeError is raised when the 'display_limit' parameter
    is not of type 'int'."""
    with pytest.raises(TypeError, match="'display_limit' parameter is not of type 'int'"):
        word_chart(test_words, display_limit="one")

def test_invalid_display_order_parameter():
    """Test that a TypeError is raised when the 'display_order' parameter
    is not of type 'str'."""
    with pytest.raises(TypeError, match="'display_order' parameter is not of type 'str'"):
        word_chart(test_words, display_order=1)

def test_invalid_display_order_values():
    """Test that a ValueError is raised when the 'display_order' parameter
    is not a valid option."""
    with pytest.raises(ValueError, match="'display_order must either be 'ascending' or 'descending'"):
        word_chart(test_words, display_order="reverse")

# test chart structure

def test_chart_is_bar():
    """Test that the chart created is a bar chart."""
    assert base_case.mark == "bar", "Resulting chart is not a bar chart."

def test_chart_titles():
    """Test that the title reflects the most or least popular words."""
    chart_asc = word_chart(test_words, display_order="ascending")
    chart_desc = word_chart(test_words, display_order="descending")
    
    chart_asc_limit = word_chart(test_words, display_limit = 3, display_order="ascending")
    chart_desc_limit = word_chart(test_words, display_limit = 15, display_order="descending")
    
    assert chart_asc.title == "The 10 Least Popular Words"
    assert chart_desc.title == "The 10 Most Popular Words"
    
    assert chart_asc_limit.title == "The 3 Least Popular Words"
    assert chart_desc_limit.title == "The 15 Most Popular Words"

def test_chart_return_type():
    """Test that the chart is an altair type."""
    assert isinstance(base_case, alt.vegalite.v5.api.Chart), "Returned output not an Altair chart."