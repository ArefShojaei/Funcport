def length(text: str) -> int:
    """
    @summary Get string length

    @desc Returns the number of characters in a string
    
    @link https://www.php.net/manual/en/function.strlen.php
    
    @example
        >>> length("Hello")
        5
    """
    if not isinstance(text, str): raise TypeError("text should be string!")

    if not text: return 0

    for index, _ in enumerate(text): pass

    return index + 1
