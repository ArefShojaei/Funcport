import re


def trim(text: str) -> str:
    pattern = r"^\s*|\s*$"
    empty_string = ""

    return re.match(pattern, text) and re.sub(pattern, empty_string, text)
