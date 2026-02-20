def contact(first_text: str, second_text: str) -> str:
    if not isinstance(first_text, str): raise TypeError("first_text should be string!")
    
    if not isinstance(second_text, str): raise TypeError("second_text should be string!")
    
    try:
        return first_text + second_text
    except ValueError:
        raise ValueError("Argument values is not valid!") from None