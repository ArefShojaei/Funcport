import re

def replace(text: str, find: str, replace: str) -> str:
    """
    @summary Replace substrings in a string
    
    @desc Replaces occurrences of a substring with another substring

    @link https://www.php.net/manual/en/function.str-replace.php

    @example
        >>> replace("Hello world", "world", "Aref")
        "Hello Aref"
    """
    return re.search(find, text) and re.sub(find, replace, text)
