def join(separator: str, list: list) -> str:
    """
    @summary Join list elements into a string

    @desc Concatenates list elements with a given separator
    
    @link https://www.php.net/manual/en/function.implode.php
    
    @example
        >>> join("-", ["a", "b", "c"])
        "a-b-c"
    """
    text = ""

    for _, word in enumerate(list):
        text += word + separator

    return text[:-len(separator)]
