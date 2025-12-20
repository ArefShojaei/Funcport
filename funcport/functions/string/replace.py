import re


def replace(text: str, find: str, replace: str) -> str:
    return re.search(find, text) and re.sub(find, replace, text)
