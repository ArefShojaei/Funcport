from .explode import explode

def pathinfo(path: str) -> dict:
    parsed_path = explode(".", path)

    dirname = parsed_path[0]
    parsed_dirname = explode("/", dirname)
    ext = parsed_path[-1]
    basename = parsed_dirname[-1] + "." + ext
    filename = parsed_dirname[-1]

    return {
        "dirname" : dirname,
        "basename" : basename,
        "filename" : filename,
        "ext" : ext,
    }