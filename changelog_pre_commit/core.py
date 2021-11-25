from typing import List

import typer

from .cli_messages import SUCCESS_MESSAGE
from .services import changelog_modifications

app = typer.Typer()


@app.command()
def main(files: List[str]):
    typer.echo(f"Files about to be analyzed: {files}")
    changelog_modifications(files)
    typer.echo(SUCCESS_MESSAGE)


def run():
    """Run commands."""
    app()
