import requests
import util
import json

ENDPOINT_CODESCANNING_ALERTS = '/code-scanning/alerts'

def run(config: dict):
    result = []

    url = config['base'] + ENDPOINT_CODESCANNING_ALERTS

    params = config.get("params", "")

    response = requests.get(url, params=params, headers = config.get('headers'), verify = config.get('verify', False))
    response = response.json()

    for res in response:
        newresponse = { 'type': 'codeql_sast', 'title': res["rule"]["description"], 'response': {}}
        newresponse['response'] = res
        newresponse = util.flatten(newresponse)
        result.append(newresponse)

    return result