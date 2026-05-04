import pytest
from funcport import string

@pytest.mark.parametrize("path", [
    "/home/aref/Desktop/scripts/server.py",
    "/app/Controllers/PostController.php",
    "/folder/image.jpeg"
])
def test_get_path_meta_data(path: str):
    meta = string.pathinfo(path)
    
    assert type(meta) == dict
    assert "dirname" in meta
    assert "basename" in meta
    assert "filename" in meta
    assert "ext" in meta