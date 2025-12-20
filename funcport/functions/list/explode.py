import re


def explode(separator: str, text: str) -> list:
    return re.split(separator, text)