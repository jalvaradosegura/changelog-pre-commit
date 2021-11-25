from typing import List

import typer

from .cli_messages import SUCCESS_MESSAGE
from .cli_options import CHANGELOG_NAME_DEFAULT
from .services import changelog_modifications

app = typer.Typer()


@app.command()
def main(files: List[str], changelog_name: str = CHANGELOG_NAME_DEFAULT):
    typer.echo(f"Files about to be analyzed: {files}")
    changelog_modifications(files, changelog_name)
    typer.echo(SUCCESS_MESSAGE)


def run():
    """Run commands."""
    app()
