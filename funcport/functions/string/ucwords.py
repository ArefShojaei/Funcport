from funcport import constants

def ucwords(text: str) -> str:
    if not isinstance(text, str): raise TypeError("text should be sring!")

    try:
        uppercase_text = ""

        for char in text:
            if char not in constants.SMALL_ALPHABET:
                uppercase_text += " "
                
                continue
            
            char_index = constants.SMALL_ALPHABET.index(char)

            uppercase_text += constants.CAPTIAL_ALPHABET[char_index]

        return uppercase_text
    except ValueError:
        raise ValueError("value is not valid") from None