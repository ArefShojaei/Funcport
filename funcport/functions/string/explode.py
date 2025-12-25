import re
from typing import List

def explode(separator: str, text: str) -> List[str]:
    """
    @summary Split string into list (PHP explode equivalent)
    
    @desc Splits a string by a given separator into a list of substrings
    
    @link https://www.php.net/manual/en/function.explode.php

    @example
        >>> explode(" ", "Hello world")
        ["Hello", "world"]

        >>> explode("*", "a*b*c")
        ["a", "b", "c"]
    """
    if not isinstance(separator, str): raise TypeError("separator should be string!")

    if not isinstance(text, str): raise TypeError("text should be string!")

    if not separator: raise ValueError("separator can not be empty!")

    escaped_separator = re.escape(separator)

    return re.split(escaped_separator, text)
