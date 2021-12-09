import pytest

from changelog_pre_commit.services import changelog_modifications


@pytest.mark.parametrize("files", [["a.py", "b.rb"], ["a.py", "b.rb", "log"]])
def test_changelog_modifications(files):
    with pytest.raises(SystemExit) as exc_info:
        changelog_modifications(files)
    assert exc_info.type == SystemExit
    assert exc_info.value.code == 1
