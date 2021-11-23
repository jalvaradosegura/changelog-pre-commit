from typer.testing import CliRunner

from changelog_pre_commit import __version__
from changelog_pre_commit.core import app


runner = CliRunner()


def test_version():
    assert __version__ == "0.1.0"


def test_app():
    result = runner.invoke(app, ["a.py", "b.rb"])
    assert result.exit_code == 0
    assert "'a.py', 'b.rb'" in result.stdout
