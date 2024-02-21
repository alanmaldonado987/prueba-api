import os

ALLOWED_EXTENSIONS = set(["json", "xlsx", "csv"])

def allowedFile(filename):
    _, extension = os.path.splitext(filename)
    if extension.lower()[1:] in ALLOWED_EXTENSIONS:
        return True
    return False