from typing import List

def join(separator: str, input: List[str]) -> str:
    """
    @summary Join list elements into a string

    @desc Concatenates list elements with a given separator
    
    @link https://www.php.net/manual/en/function.implode.php
    
    @example
        >>> join("-", ["a", "b", "c"])
        "a-b-c"
    """
    if not isinstance(separator, str): raise TypeError("separator should be string!")

    if not isinstance(input, list): raise TypeError("input should be list of string!")

    if len(input) <= 1: raise ValueError("input size can not be less than 2!")

    if not separator: raise ValueError("separator can not be empty!")

    text = ""

    for _, word in enumerate(input):
        if not isinstance(word, str): raise ValueError("each input data should be string!")

        text += word + separator

    return text[:-len(separator)]
