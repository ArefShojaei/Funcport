import re

def trim(text: str) -> str:
    """
    @summary Trim function (Python version of PHP's trim)

    @desc Removes whitespaces from the beginning and end of a string

    @link https://www.php.net/manual/en/function.trim.php

    @example
        >>> trim(" Hello")
        "Hello"

        >>> trim("Hello ")
        "Hello"

        >>> trim(" Hello ")
        "Hello"
    """
    if not isinstance(text, str): raise TypeError("Invalid input data type!")
    
    if not len(text): return text

    pattern = r"^\s*|\s*$"
    empty_string = ""

    return re.match(pattern, text) and re.sub(pattern, empty_string, text)
