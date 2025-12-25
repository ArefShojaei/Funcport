def split(text: str) -> list:
    """
    @summary Split string into list
    
    @desc Splits a string by whitespace or a given separator

    @link https://docs.python.org/3/library/stdtypes.html#str.split
    
    @example
        >>> split("Hello")
        ["H", "e", "l", "l", "o"]
    """
    return [char for _, char in enumerate(text)]
