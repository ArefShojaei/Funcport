from funcport import constants

def ucfirst(text: str) -> str:
    """
    @summary Get the string with its first character converted to uppercase

    @desc
        Returns a new string where the first character is converted to uppercase (if it is a letter),
        and the rest of the string remains unchanged.
        If the string is empty, an empty string is returned.
        This function is similar to PHP's ucfirst() or behaves like a "true" ucfirst,
        unlike Python's built-in str.capitalize() which also lowercases the remaining characters.

        The input must be a string; otherwise, a TypeError is raised.

    @link https://www.php.net/manual/en/function.ucfirst.php

    @example
        >>> ucfirst("hello")
        'Hello'

        >>> ucfirst(" hello")
        ' hello'

        >>> ucfirst("python is great")
        'Python is great'

        >>> ucfirst("a")
        'A'

        >>> ucfirst("A")
        'A'
    """
    if not isinstance(text, str): raise TypeError("text should be sring!")

    try:
        first_char = text[0]

        if first_char not in constants.SMALL_ALPHABET: return text
        
        char_index = constants.SMALL_ALPHABET.index(first_char)

        uppercase_char = constants.CAPTIAL_ALPHABET[char_index]

        return uppercase_char + text[1:]
    except ValueError:
        raise ValueError("value is not valid") from None