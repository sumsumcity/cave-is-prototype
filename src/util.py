import json
from dotenv import load_dotenv # type: ignore
import os

def loadConfig(file: str):
    result = {'include': file}
    dictmap(result, processincludes)
    result = loadEnv(result)
    return result

def loadEnv(file: dict) -> dict:
    jsonstr = json.dumps(file)
    load_dotenv()
    jsonstr = jsonstr.replace("${MYSQL_PASSWORD}", os.getenv("MYSQL_PASSWORD"))
    file = json.loads(jsonstr)
    return file


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