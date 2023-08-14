# Directory Spell Checker

This script provides a robust solution for spell-checking files within a directory. It has an interactive CLI for corrections, supports custom dictionaries, backups, configuration files, and even integrates with Git!

## Features

- **Interactive CLI**: On detecting a misspelled word, the script allows you to ignore, correct or replace with a suggested word.
- **Backup Option**: Before making corrections, the original file is backed up with a `.bak` extension.
- **Custom Dictionaries**: Add your industry-specific terms to ensure they aren't flagged as errors.
- **Configuration File Support**: Use a JSON configuration file to specify custom dictionary words and other settings.
- **Git Integration**: The script can automatically commit changes to a Git repository.

## Prerequisites

- Python 3.x
- Required Python packages: `spellchecker`, `tqdm`, `gitpython`
  ```bash
  pip install pyspellchecker tqdm gitpython
  ```

## Example Usage

1. Clone the repository:
    ```bash
    git clone https://github.com/jbar2797/Spell-Checker-for-Directories.git
    cd Spell-Checker-for-Directories
    ```

2. Let's say you have a directory named `MyDocs` in the `C:\Users\Alice\Documents` path and you want to check `.txt` and `.md` files for spelling errors. Additionally, you want to include subdirectories in the check and use a configuration file named `config.json`.

Navigate to the directory where the `spell_check_script.py` script is located and run the following command ( this is where you cloned the repo ):

```bash
python spell_check_script.py --path C:\Users\Alice\Documents\MyDocs --extensions .txt,.md --subdirs --config config.json
```

Explanation:

- `--path C:\Users\Alice\Documents\MyDocs`: This specifies the directory you want to spell-check.
  
- `--extensions .txt,.md`: This tells the script to only check files that have the `.txt` and `.md` extensions.
  
- `--subdirs`: This flag tells the script to also scan and check files inside subdirectories of `MyDocs`.
  
- `--config config.json`: This uses `config.json` as the configuration file for custom dictionary words and other settings.

After running the script, you'll be interactively prompted for actions on any misspelled words it detects. Once done, if you have enabled the Git option in the configuration file and your directory is a Git repository, the script will automatically commit the changes.


### Arguments

- `--path` : Specify the directory path to check (default is the current directory).
- `--extensions` : Comma-separated file extensions to check (default is `.txt`).
- `--subdirs` : If included, the script will also scan subdirectories.
- `--config` : Path to the configuration file (default is `config.json`).

### Configuration File (`config.json`)

You can use a configuration file to specify custom dictionary words and other settings (dictionary will be empty and git_commit will be false by default):

```json
{
    "custom_dictionary": ["specificWord1", "specificWord2"],
    "git_commit": true
}
```

## Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss the change you'd like to make.

## License

MIT License. See [LICENSE](LICENSE) for more information.
