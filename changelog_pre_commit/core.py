from typing import List

import typer

app = typer.Typer()


@app.command()
def main(files: List[str]):
    typer.echo(f"Files about to be analyzed: {files}")
