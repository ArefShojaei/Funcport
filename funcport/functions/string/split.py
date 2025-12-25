def split(text: str) -> list:
    """
    @summary Split string into list
    
    @desc Splits a string by whitespace or a given separator

    @link https://docs.python.org/3/library/stdtypes.html#str.split
    
    @example
        >>> split("Hello")
        ["H", "e", "l", "l", "o"]
    """
    if not isinstance(text, str): raise TypeError("Invalid input data type!")

    if not len(text): return []

    return [char for _, char in enumerate(text)]
