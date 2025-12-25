def repeat(text: str, length: int) -> str:
    """
    @summary Repeat a string multiple times
    
    @desc Returns a new string repeated a given number of times
    
    @link https://www.php.net/manual/en/function.str-repeat.php

    @example
        >>> repeat("Hello ", 2)
        "Hello Hello"
    """
    if not isinstance(text, str): raise TypeError("text should be string!")

    if not isinstance(length, int): raise TypeError("length should be int!")

    if text == "" : raise ValueError("text should not be empty!")
    
    if length <= 0 : raise ValueError("length should not be zero or negative!")
    
    return text * length