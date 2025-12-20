import re


def contains(text: str, search: str) -> bool:
    return True if re.search(search, text) else False
