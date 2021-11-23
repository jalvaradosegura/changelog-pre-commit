from typing import List

import typer

from .services import changelog_modifications

app = typer.Typer()


@app.command()
def main(files: List[str]):
    typer.echo(f"Files about to be analyzed: {files}")
    changelog_modifications(files)


def run():
    """Run commands."""
    app()
