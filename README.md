# Text Parsing Package

## Contributors:

* Jacob Cann (@Jacob-F-Cann)
* Rebecca Sokol-Snyder (@rsokolsnyder)
* Wes Beard (@beardw)

## Summary

The following package aims to aid in the parsing of text data, by providing functions to clean, analyze and visualize text data.
The goal of the package is to simplify and streamline text processing, such that in a few lines of code the user can easily understand
what the text data they are working with looks like.

Since processing, analyzing and visualizing text data is so common, this package
provides and alternative to existing packages in the Python ecosystem with specific, but configurable stylistic choices.

Ease of use and development speed using the package functions will be a major advantage of the this package over others at the expense of a bit of generalization, which is already available in many other packages (see examples in *Relation to Existing Package Ecosystem*  below).

The functions implemented will be tested against other existing solutions to validate their outputs as being correct, making their use
being a stylistic design choice rather than different functionality altogether.

## Package Functions

1. A function to clean/preprocess a block of input text data.

    * The function will remove punctuation and set all words to lower case for easier analysis, for example to obtain the counts of each of the unique words that appear in the text.
    * Options for how the text block shall be processed will be included in the function as optional arguments.
    * The function will be implemented such that it can be used independently of the other functions in this package or the following functions below may be used sequentially.

2. A function to count the number instances of unique words in a block of cleaned input text data.

    * The function will return a dictionary of unique words as keys and their corresponding values will contain the counts of the word in the input text.
    * Optional arguments for the function will modify the return of the counts based on user input, for example ignoring certain words for counting.
    * The function will be implemented such that it can be used independently of the other functions in this package or used sequentially, provided that the input text data is in a compatible format or has been preprocessed using the function in the package.

3. A function to visualize the top counts or frequencies of occurrence of the words within the input text.

    * The function will return a bar plot of the frequencies of the top words for ease of visualization, formatted with proper data visualization practices.
    * Optional arguments will control what is displayed in the plot generated, for example the maximum number of words to display.
    * The function will be implemented such that it can be used independently of the other functions in this package or used sequentially, provided the input is in the proper format.

## set up the development environment (environment.yml)

## Installation

```bash
pip install text_parsing_package
```

## Usage

The `text_parsing_package` is used to clean text, count the words, and plot the results on a bar chart.

```python
from text_parsing_package.clean_text import clean_text
from text_parsing_package.count_words import count_unique_words
from text_parsing_package.word_chart import word_chart

text = "The quick brown fox jumped over the fence."
text_clean = clean_text(text)
text_count = count_unique_words(text_clean)
bar_fig = word_chart(text_count)
bar_fig # output an altair bar plot
```

## Run Tests

To run the test suite, following these steps:

1. Ensure you have the development environment installed and activated.
2. Enter the following command in your terminal.

 ```bash
$ pip install text_parsing_package -e .[tests]
```

3. Once the package has installed with test package requirements, run the following command in your terminal.

```bash
$ pytest
```

4. Test(s) success and/or failure will be output to the terminal.

## Build Documentation

To build the documentation, follow the following steps:

1. Ensure you have the development environment installed and activated.
2. Enter the following command in your terminal.

 ```bash
$ pip install text_parsing_package -e .[docs]
```

3. Once the package has been loaded with the appropriate dependencies, run the following command in your terminal:

```bash
$ quartodoc build
```

4. To preview the documentation, run this command:

```bash
$ quarto preview
```

## Deploy Documentation (automated)

## Relation to Existing Package Ecosystem

There exists other packages in the Python ecosystem which are capable of performing in essence the same tasks as this package, however there are stylistic implementation differences, for which the end-user may prefer. Overall, the landscape for text processing is quite saturated in the python ecosystem. This is due to text parsing being such a common task and the Python ecosystem being so vast. For example, the visualization packages for text data that exist already are not as specific as the implementation contained in this package, they are more generic but may require more lines of code to reproduce the output of this package.

Similarly, the text cleaning/preprocessing functionality of this package likely does not exist already in the ecosystem in the exact same implementation and may have stylistic differences, but similar operations can be done with other packages to obtain the same modified text string. The unique word count functionality of this package is likely implemented differently "under the hood" than other solutions present in the ecosystem in the same way, but will produce the same final output as existing packages. Examples of existing packages are shown below (not an exhaustive list):

### Package Examples

#### Text visualization

1. [WordCloud](https://pypi.org/project/wordcloud/)
2. [Scattertext](https://pypi.org/project/scattertext/)

#### Text cleaning/preprocessing

1. [CleanText](https://pypi.org/project/cleantext/)
2. [clean-text](https://pypi.org/project/clean-text/)

#### Text analysis

1. [NLTK](https://pypi.org/project/nltk/)
2. [spaCy](https://pypi.org/project/spacy/)

### License

The software code contained within this repository is licensed under the [MIT license](https://spdx.org/licenses/MIT.html). See the license file for more information.
