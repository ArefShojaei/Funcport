from .explode import explode
from ..list.count import count

def word_count(text: str) -> int:
    if not isinstance(text, str): raise TypeError("text should be string!")

    parsed_text = explode(" ", text)

    return count(parsed_text)
