def repeat(text: str, length: int):
    """
    @summary Repeat a string multiple times
    
    @desc Returns a new string repeated a given number of times
    
    @link https://www.php.net/manual/en/function.str-repeat.php

    @example
        >>> repeat("Hello ", 2)
        "Hello Hello"
    """
    result = ""
    
    for _ in range(0, length):
        result += text

    return result
