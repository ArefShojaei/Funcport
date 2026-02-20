def reverse(text: str) -> str:
    if not isinstance(text, str): raise TypeError("text should be string!")

    current_string_length = len(text)

    reversed_text = ""

    for _ in text:
        current_string_length -= 1
        
        reversed_text += text[current_string_length]

    return reversed_text