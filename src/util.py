import json

def loadConfig(file: str):
    result = {'include': file}
    dictmap(result, processincludes)
    return result

def loadJson(file: str) -> dict:
    with open(file) as f:
        return json.load(f)

def processincludes(d: dict):
    if 'include' in d:
        for k, v in loadJson(d['include']).items():
            if not k in d:
                d[k] = v
        del d['include']

def dictmap(d: dict, fn):
    fn(d)
    for k, v in d.items():
        if isinstance(v, dict):
            dictmap(v, fn)