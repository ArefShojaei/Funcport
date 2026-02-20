from funcport import constants

def lcwords(text: str) -> str:
    if not isinstance(text, str): raise TypeError("text should be sring!")

    try:
        lowercase_text = ""

        for char in text:
            if char not in constants.CAPTIAL_ALPHABET:
                lowercase_text += " "
                
                continue
            
            char_index = constants.CAPTIAL_ALPHABET.index(char)

            lowercase_text += constants.SMALL_ALPHABET[char_index]

        return lowercase_text
    except ValueError:
        raise ValueError("value is not valid") from None