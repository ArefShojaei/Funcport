from typing import Any

def current(hystack: list) -> Any:
    if not isinstance(hystack, list): raise TypeError("hystack should be list!")
    
    return hystack[0]