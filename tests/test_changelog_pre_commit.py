from unittest.mock import patch

from typer.testing import CliRunner

from changelog_pre_commit import __version__
from changelog_pre_commit.core import app, run


runner = CliRunner()


def test_version():
    assert __version__ == "0.1.0"


def test_main():
    result = runner.invoke(app, ["a.py", "b.rb"])
    assert result.exit_code == 0
    assert "'a.py', 'b.rb'" in result.stdout


@patch("changelog_pre_commit.core.app", lambda: "I was mocked")
def test_run():
    run()
