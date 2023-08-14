# SPELL CHECKER FOR DIRECTORIES

This script provides a simple yet effective way to check spelling in text files within a specified directory (and optionally its subdirectories). It uses the **'pyspellchecker'** library for spell checking, **'tqdm'** for progress visualization, and **'chardet'** to handle file encoding detection.

## Features

- User-specified directory for spell checking.
- Option to specify file extensions to be checked.
- Can recursively check subdirectories if chosen by the user.
- Detects and provides context (line number and the line itself) for each spelling error.
- Handles different file encodings gracefully.
- Outputs errors both to the console and to a log file.

## Installation

First, you need to clone this repository:
`git clone [Your Repository URL]
cd [Your Repository Directory Name]`

Install the required libraries:
`pip install pyspellchecker tqdm chardet`

## Usage

Run the script:
`python spell_check_directory.py`

Follow the prompts to specify the directory, file extensions, and whether to include subdirectories.

After the scan is complete, if any spelling errors are detected, they will be displayed in the console and saved to a **'spelling_errors.log'** file inside a **'log'** folder within the specified directory.

## Contributions

Contributions are welcome! Please feel free to submit a pull request or open an issue to discuss potential improvements or fixes.
