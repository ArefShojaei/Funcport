def count(input: list) -> int:
    """
    @summary Count occurrences of a substring
    
    @desc Returns the number of times a substring appears in a string

    @link https://www.php.net/manual/en/function.substr-count.php

    @example
        >>> count([1,2,3])
        3

        >>> count(["a", "b"])
        2

        >>> count([])
        0
    """
    if not isinstance(input, list): raise TypeError("input should be list!")

    count = 0

    for _ in input:
        count += 1
    
    return count
