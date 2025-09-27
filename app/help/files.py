import json
from slugify import slugify
from saas.settings import BASE_DIR
TEMPFILES = 'data'

def save_to_file(respons, filepath: str, type: str):
    path = BASE_DIR.parent / TEMPFILES / filepath
    with open(path, 'w') as f:
        if type == 'json':
            f.write(json.dumps(respons))
        else:
            f.write(respons)
        f.close()

def load_from_file(filepath: str, type: str):
    path = BASE_DIR.parent / TEMPFILES / filepath
    with open(path, 'r') as f:
        if type == 'json':
            d = json.load(f)
        else:
            d = f.read()
    return d