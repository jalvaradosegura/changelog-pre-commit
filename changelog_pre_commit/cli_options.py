import typer

CHANGELOG_NAME_DEFAULT = typer.Option(
    "changelog",
    help="Name of the changelog file that will be searched for changes",
)
