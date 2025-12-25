import re
from typing import Union


def replace(text: str, find: str, replace: str) -> Union[str, None]:
    """
    @summary Replace substrings in a string
    
    @desc Replaces occurrences of a substring with another substring

    @link https://www.php.net/manual/en/function.str-replace.php

    @example
        >>> replace("Hello world", "world", "Aref")
        "Hello Aref"
    """
    if not isinstance(text, str): raise TypeError("text should be string!")
    
    if not isinstance(find, str): raise TypeError("find should be string!")
    
    if not isinstance(replace, str): raise TypeError("replace should be string!")

    return re.search(find, text) and re.sub(find, replace, text)
