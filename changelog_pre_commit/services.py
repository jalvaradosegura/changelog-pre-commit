from typing import List

from .utils import contains_changelog_file


def changelog_modifications(files: List):
    if not contains_changelog_file(files):
        raise Exception("You didn't modify the changelog file")
