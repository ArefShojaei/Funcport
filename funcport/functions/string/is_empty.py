def is_empty(text: str) -> bool:
    if not isinstance(text, str): raise TypeError("text should be string!")
    
    return False if len(text) else True