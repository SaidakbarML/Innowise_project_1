import json

def load_json(path):
    with open(path) as r:
        return json.load(r)


