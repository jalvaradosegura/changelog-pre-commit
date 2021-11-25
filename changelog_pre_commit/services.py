import sys
from typing import List

import typer

from .cli_messages import ERROR_MESSAGE
from .utils import contains_changelog_file


def changelog_modifications(files: List):
    if not contains_changelog_file(files):
        typer.echo(ERROR_MESSAGE)
        sys.exit(1)
