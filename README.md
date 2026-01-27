# Text Parsing Package

## Summary

This package aims to aid in the parsing of text data, by providing functions to clean, analyze and visualize text data. For further details about this project, please refer to our [About](https://ubc-mds.github.io/text-parsing-package/docs/about.html) page.

## Functions

* `clean_text()`
  * removes punctuation and set all words to lower case for easier analysis
* `count_unique_words()`
  * counts the number instances of unique words in a block of cleaned input text data
* `word_chart()`
  * visualize the top counts of the words within the input in the form of a bar chart

## Installation

1. To install this package, navigate to your preferred environment.
2. Run the following command in your terminal.

```bash
pip install -i https://test.pypi.org/simple/ text-parsing-package
```
The TestPyPI home page can be viewed [here](https://test.pypi.org/project/text-parsing-package/) and the source distribution
can be downloaded [here](https://test.pypi.org/project/text-parsing-package/#files). 

## Usage

Below are examples of how the `text_parsing_package` can be used to clean text, count the words, and plot the results onto a bar chart.

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

## Contributing

To contribute to this project, check out [Contributing](https://ubc-mds.github.io/text-parsing-package/CONTRIBUTING.html).

If you would like to run the tests, and, build and deploy documentation, read below.

### Clone Repository and Install Package with Development Dependencies

1. Clone this [repository](https://github.com/UBC-MDS/text-parsing-package) and activate the environment.

```bash
git clone git@github.com:UBC-MDS/text-parsing-package.git
```

Creating the environment is not required, but if you would like you can this way. Make sure to be in the root directory.

```bash
conda env create -n text_parsing -f environment.yml
conda activate text_parsing
```

2. Navigate to the root of the project directory and install package with dependencies.

Not all dependecies have to be installed, depending on your goal.

```bash
pip install -e .[tests,dev,docs]
```

### Run Tests

 ```bash
pytest --cov=src --cov-branch --cov-report=term-missing
```

### Build, Preview, and Deploy the Documentation

1. Build and preview the documentation.

```bash
quartodoc build
quarto preview
```

2. To update the documentation website.

```bash
quarto publish gh-pages
```

## Relation to Existing Package Ecosystem

Refer to our [About](https://ubc-mds.github.io/text-parsing-package/docs/about.html) page.

## Contributors

* Jacob Cann (@Jacob-F-Cann)
* Rebecca Sokol-Snyder (@rsokolsnyder)
* Wes Beard (@beardw)

### License

The software code contained within this repository is licensed under the [MIT license](https://spdx.org/licenses/MIT.html). See the license file for more information.
