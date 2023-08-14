import os
from spellchecker import SpellChecker
from tqdm import tqdm
import chardet

def detect_file_encoding(file_path):
    with open(file_path, 'rb') as f:
        result = chardet.detect(f.read())
        return result['encoding']

def check_spelling_in_file(file_path):
    spell = SpellChecker()
    encoding = detect_file_encoding(file_path)
    errors = {}

    with open(file_path, 'r', encoding=encoding, errors='replace') as f:
        for line_num, line in enumerate(f, 1):
            words = line.split()
            misspelled = spell.unknown(words)
            if misspelled:
                context = line.strip()
                for word in misspelled:
                    errors[word] = (line_num, context)

    return errors

def main():
    folder = input("Please enter the folder path: ")
    ext_filter = input("Enter file extensions to check (comma separated, e.g. .txt,.md) or leave blank for all: ").split(',')
    scan_subdirectories = input("Do you want to scan subdirectories as well? (yes/no): ").lower().strip() == 'yes'

    if not os.path.exists(folder):
        print(f"The folder {folder} does not exist!")
        return

    files = []
    if scan_subdirectories:
        for dirpath, _, filenames in os.walk(folder):
            for f in filenames:
                if not ext_filter or any(f.endswith(ext) for ext in ext_filter):
                    files.append(os.path.join(dirpath, f))
    else:
        for f in os.listdir(folder):
            if os.path.isfile(os.path.join(folder, f)) and (not ext_filter or any(f.endswith(ext) for ext in ext_filter)):
                files.append(os.path.join(folder, f))

    error_dict = {}
    print("Checking spelling in files...")
    for file in tqdm(files):
        errors = check_spelling_in_file(file)
        if errors:
            error_dict[file] = errors

    num_checked = len(files)
    num_errors = len(error_dict)

    print(f"\n{num_checked} files were checked.")
    if num_errors == 0:
        print("No spelling errors found.")
    else:
        print(f"Found spelling errors in {num_errors} files.")
        for file, errors in error_dict.items():
            print(f"\nFile: {file}")
            for word, (line_num, context) in errors.items():
                print(f"Error: {word} (Line: {line_num}, Context: '{context}')")

        log_folder = os.path.join(folder, 'log')
        if not os.path.exists(log_folder):
            os.mkdir(log_folder)

        with open(os.path.join(log_folder, 'spelling_errors.log'), 'w', encoding="utf-8") as log:
            for file, errors in error_dict.items():
                log.write(f"File: {file}\n")
                for word, (line_num, context) in errors.items():
                    log.write(f"Error: {word} (Line: {line_num}, Context: '{context}')\n")
                log.write("\n")

if __name__ == '__main__':
    main()
