from typing import List


def contains_changelog_file(files: List):
    for file in files:
        if "changelog" in file.lower():
            return True
    return False
