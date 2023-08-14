import os
import argparse
from spellchecker import SpellChecker
from tqdm import tqdm
import json
from git import Repo

def backup_file(file_path):
    backup_path = file_path + '.bak'
    with open(file_path, 'rb') as original, open(backup_path, 'wb') as backup:
        backup.write(original.read())

def check_and_correct_spelling(file_path, custom_dict):
    spell = SpellChecker()
    spell.word_frequency.load_words(custom_dict)
    errors = {}

    with open(file_path, 'r', errors='replace') as f:
        lines = f.readlines()

    for line_num, line in enumerate(lines, 1):
        words = line.split()
        misspelled = spell.unknown(words)
        if misspelled:
            for word in misspelled:
                print(f"Misspelled word '{word}' found in {file_path} on line {line_num}: {line.strip()}")
                action = input("Action [ignore (i), correct (c), replace with suggestion (r)]: ")
                if action == 'c':
                    correct = input(f"Enter correction for {word}: ")
                    lines[line_num - 1] = lines[line_num - 1].replace(word, correct)
                elif action == 'r':
                    suggestions = spell.candidates(word)
                    if suggestions:
                        print(f"Suggestions: {', '.join(suggestions)}")
                        choice = input("Enter your choice or leave blank to skip: ")
                        if choice in suggestions:
                            lines[line_num - 1] = lines[line_num - 1].replace(word, choice)

    with open(file_path, 'w', errors='replace') as f:
        f.writelines(lines)

    return errors

def main():
    parser = argparse.ArgumentParser(description="Spell Checker for Directories")
    parser.add_argument('--path', type=str, default='.', help='Directory path to check')
    parser.add_argument('--extensions', type=str, default='.txt', help='Comma separated file extensions to check')
    parser.add_argument('--subdirs', action='store_true', help='Include subdirectories')
    parser.add_argument('--config', type=str, default='config.json', help='Path to the configuration file')
    
    args = parser.parse_args()

    # Load configuration
    config = {}
    if os.path.exists(args.config):
        with open(args.config, 'r') as config_file:
            config = json.load(config_file)

    custom_dict = config.get('custom_dictionary', [])
    git_commit = config.get('git_commit', False)

    files_to_check = []
    if args.subdirs:
        for dirpath, _, filenames in os.walk(args.path):
            for file in filenames:
                if file.endswith(tuple(args.extensions.split(','))):
                    files_to_check.append(os.path.join(dirpath, file))
    else:
        for file in os.listdir(args.path):
            if os.path.isfile(os.path.join(args.path, file)) and file.endswith(tuple(args.extensions.split(','))):
                files_to_check.append(os.path.join(args.path, file))

    for file in tqdm(files_to_check, desc="Processing files"):
        backup_file(file)  # Backup original file
        check_and_correct_spelling(file, custom_dict)

    # Git Integration
    if git_commit:
        try:
            repo = Repo(args.path)
            repo.git.add(update=True)
            repo.index.commit("Auto commit after spell check.")
            print("Committed the changes to the repository.")
        except:
            print("Failed to commit changes. Ensure the directory is a git repository.")

if __name__ == '__main__':
    main()
