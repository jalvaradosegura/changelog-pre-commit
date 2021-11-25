from typing import List


def contains_changelog_file(
    files: List[str], changelog_name: str = "changelog"
) -> bool:
    for file in files:
        if changelog_name in file.lower():
            return True
    return False
