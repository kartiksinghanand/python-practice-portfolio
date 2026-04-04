from typing import List


# Day 7 - Problem 4
# Topic: String processing
#
# Task:
# Given a list of filenames, return only the filenames that end with ".py"
# or ".txt".
#
# Important:
# - keep original order
# - ignore other extensions
#
# What to return:
# - only filenames ending with ".py" or ".txt"
#
# Expected output for current sample:
# ["main.py", "notes.txt", "report.txt"]


files = ["main.py", "notes.txt", "image.png", "script.js", "report.txt"]


def allowed_files(files: List[str]) -> List[str]:
    required_files = []
    for file in files:
        name, extension = file.split(".")
        if extension == "py" or extension == "txt":
            required_files.append(file)
    return required_files

if __name__ == "__main__":
    print(allowed_files(files))
