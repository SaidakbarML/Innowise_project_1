import json

def load_json(path): # open json file and return python data
    with open(path) as r:
        return json.load(r)


