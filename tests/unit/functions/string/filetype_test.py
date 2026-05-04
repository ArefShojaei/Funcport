import pytest
from funcport import string

@pytest.mark.parametrize("file, exptected", [
    ("server.php", "php"),
    ("plugin.js", "js"),
    ("photo.png", "png"),
    ("app.go", "go"),
])
def test_get_file_extention_of_file_string(file: str, exptected: str):
    file_extention = string.filetype(file)

    assert file_extention == exptected
    assert len(file_extention) == len(exptected)