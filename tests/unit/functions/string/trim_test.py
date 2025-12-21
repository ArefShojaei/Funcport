from funcport import string


def test_trim_whitespace():
    text = " Hello "
    excepted = "Hello"

    value = string.trim(text)

    assert value != text
    assert value == excepted

def test_trim_empty_sring():
    text = ""

    value = string.trim(text)

    assert value == text    

def test_trim_no_change():
    text = "Hello"

    value = string.trim(text)

    assert value == text

def test_trim_start_string():
    text = " Hello"
    excepted = "Hello"

    value = string.trim(text)

    assert value != text
    assert value == excepted

def test_trim_end_string():
    text = "Hello "
    excepted = "Hello"

    value = string.trim(text)

    assert value != text
    assert value == excepted