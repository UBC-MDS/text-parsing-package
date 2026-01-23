# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).


## [0.0.1] - (2026-01-10)

- First release

### Changes Added by @Jacob-F-Cann
- Function description/specification written without code implementation for count_unique_words() in count_words.py
- README.md Milestone 1 Sections added detailing the package summary, included functions and relation to Python ecosystem.

### Changes Added by @rsokolsnyder
- Function description/specification written without code implementation for clean_text() in clean_text.py
- CONTRIBUTING.MD updated to remove bug fix and feature implementations

### Changes Added by @beardw
- Function description/specification written without code implementation for word_chart() in word_chart.py
- Added a reference in CONTRIBUTING.md to the CODE_OF_CONDUCT.md.
- Updated CODE_OF_CONDUCT.md contact individuals.

## [0.0.2] - (2026-01-17)

- Second release

### Changes Added by @Jacob-F-Cann
- Write the initial count_unique_words function implementation
- Write unit tests for expected and unexpected input to the count_unique_words function
- Validate tests pass using pytest commands and add dependencies to pyproject.toml

### Changes Added by @rsokolsnyder
- Write function implementation for clean_text() in clean_text.py
- Add unit tests for clean_text() in test_clean_text.py
- Add dependencies to pyproject.toml


### Changes Added by @beardw
- Write word_chart.py function internals.
- Implement unit tests for word_chart.py.
- Added word_chart.py package dependencies to pyproject.toml

## [0.0.3] - (2026-01-23)

- Third release

### Changes Added by @rsokolsnyder
- Add GitHub Action to run test suite
- Add additional tests and exception handling for clean_text()

### Changes Added by @Jacob-F-Cann
- Add GitHub Action to deploy the package to Test PyPI
- Accept and validate suggested tweaks to count_unique_words() 
  implementation and additional tests given by ChatGPT 5.2 LLM. 
  Changes and exact model input/output are tracked in the 
  docs/misc/ChatGPT_prompt_log.md file in the repository.
