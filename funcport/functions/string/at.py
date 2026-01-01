def at(text: str, index: int) -> str:
    """
    @summary Get character at specific index in a string

    @desc
        Returns the single character at the given index in the string.
        Supports both positive and negative indices (like standard Python indexing).
        Raises TypeError if inputs are not of correct type, and IndexError if index is out of range.

    @link https://www.w3schools.com/jsref/jsref_array_at.asp

    @example
        >>> at("hello", 0)
        'h'

        >>> at("hello", 4)
        'o'

        >>> at("python", -1)
        'n'

        >>> at("abc", -3)
        'a'

        >>> at("", 0)
        Traceback (most recent call last):
        IndexError: string index out of range: 0

        >>> at("text", 10)
        Traceback (most recent call last):
        IndexError: string index out of range: 10
    """
    if not isinstance(text, str): raise TypeError("text should be string!")
    
    if not isinstance(index, int): raise TypeError("index should be int!")
    
    try:
        return text[index]
    except IndexError:
        raise IndexError(f"string index out of range: {index}") from None