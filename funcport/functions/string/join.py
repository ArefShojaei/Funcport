def join(separator: str, list: list) -> str:
    text = ""

    for _, word in enumerate(list):
        text += word + separator

    return text[:-len(separator)]