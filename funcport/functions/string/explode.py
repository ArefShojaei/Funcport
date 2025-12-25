import re

def explode(separator: str, text: str) -> list:
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
    return re.split(separator, text)
