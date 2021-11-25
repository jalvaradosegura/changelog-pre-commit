import typer

_SUCCESS_START = "Everything is "
_SUCCESS_END = typer.style("ok ", fg=typer.colors.GREEN, bold=True)
_SUCCESS_EMOJIS = "✨🍕"
SUCCESS_MESSAGE = _SUCCESS_START + _SUCCESS_END + _SUCCESS_EMOJIS


_ERROR_START = typer.style(
    "Changelog not updated", bg=typer.colors.RED, bold=True
)
_ERROR_END = "...Please update the file "
_ERROR_EMOJIS = "🔍🧐"
ERROR_MESSAGE = _ERROR_START + _ERROR_END + _ERROR_EMOJIS
