import re

def contains(text: str, search: str) -> bool:
    """
    @summary Check if substring exists in string
    
    @desc Returns True if the substring is found, otherwise False
    
    @link https://www.php.net/manual/en/function.strpos.php

    @example
        >>> contains("Hello World", "World")
        True

        >>> contains("Hello World", "Python")
        False
    """
    if not isinstance(text, str): raise TypeError("text should be string!")
    
    if not isinstance(search, str): raise TypeError("search should be string!")

    return True if re.search(search, text) else False
