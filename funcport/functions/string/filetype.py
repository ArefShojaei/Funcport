from .explode import explode

def filetype(file: str):
    if not isinstance(file, str): raise TypeError("file should be string!")

    parsed_file = explode(".", file)

    return parsed_file[-1]