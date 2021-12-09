import pytest

from changelog_pre_commit.utils import contains_changelog_file


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
