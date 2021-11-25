from unittest.mock import patch

import pytest
from typer.testing import CliRunner

from changelog_pre_commit import __version__
from changelog_pre_commit.core import app, run
from changelog_pre_commit.services import changelog_modifications
from changelog_pre_commit.utils import contains_changelog_file

runner = CliRunner()


def test_version():
    assert __version__ == "0.3.0"


def test_main_exit_0():
    result = runner.invoke(app, ["a.py", "b.rb", "changelog"])
    assert result.exit_code == 0
    assert "'a.py', 'b.rb'" in result.stdout


def test_main_exit_1():
    result = runner.invoke(app, ["a.py", "b.rb"])
    assert result.exit_code == 1
    assert "'a.py', 'b.rb'" in result.stdout


@patch("changelog_pre_commit.core.app", lambda: "I was mocked")
def test_run():
    run()


@pytest.mark.parametrize(
    "files, changelog_name",
    [
        (["a.py", "b.rb"], "changelog"),
        (["a.py", "b.rb", "log"], "changelog"),
        (["a.py", "changelog", "log"], "here_are_my_changes"),
    ],
)
def test_check_for_changelog_file_and_there_is_no_changelog(
    files, changelog_name
):
    result = contains_changelog_file(files, changelog_name)
    assert result is False


@pytest.mark.parametrize(
    "files, changelog_name",
    [
        (["a.py", "b.rb", "changelog"], "changelog"),
        (["a.py", "Changelog.md", "log"], "changelog"),
        (["a.py", "CHANGELOG.MD", "log"], "changelog"),
        (["a.py", "my_changes.md", "log"], "my_changes"),
        (["a.py", "b.js", "hi_changelog.py"], "changelog"),
    ],
)
def test_check_for_changelog_file_and_there_is_a_changelog(
    files, changelog_name
):
    result = contains_changelog_file(files, changelog_name)
    assert result is True


@pytest.mark.parametrize("files", [["a.py", "b.rb"], ["a.py", "b.rb", "log"]])
def test_changelog_modifications(files):
    with pytest.raises(SystemExit) as exc_info:
        changelog_modifications(files)
    assert exc_info.type == SystemExit
    assert exc_info.value.code == 1
