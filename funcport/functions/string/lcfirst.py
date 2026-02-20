from funcport import constants

def lcfirst(text: str) -> str:
    """
    @summary Get the string with its first character converted to lowercase

    @desc
        Returns a new string where the first character is converted to lowercase (if it is a letter),
        and the rest of the string remains unchanged.
        If the string is empty, an empty string is returned.
        This function is similar to PHP's lcfirst(), providing a "true" lowercase-first behavior.
        Unlike Python's built-in str.lower(), it only affects the first character and preserves
        the original casing of the remaining characters.

        The input must be a string; otherwise, a TypeError is raised.

    @link https://www.php.net/manual/en/function.lcfirst.php

    @example
        >>> lcfirst("Hello")
        'hello'

        >>> lcfirst("Python is great")
        'python is great'

        >>> lcfirst("A")
        'a'

        >>> lcfirst("a")
        'a'

        >>> lcfirst("")
        ''

        >>> lcfirst(" Hello")
        ' Hello'
    """
    if not isinstance(text, str): raise TypeError("text should be sring!")

    try:
        first_char = text[0]

        if first_char not in constants.CAPTIAL_ALPHABET: return text
        
        char_index = constants.CAPTIAL_ALPHABET.index(first_char)

        lowercase_char = constants.SMALL_ALPHABET[char_index]

        return lowercase_char + text[1:]
    except ValueError:
        raise ValueError("value is not valid") from None