def values(object: dict) -> list:
    return [object[key] for _, key in enumerate(object)]