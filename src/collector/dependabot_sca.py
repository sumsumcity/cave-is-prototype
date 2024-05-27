import requests
import util
import json

ENDPOINT_DEPENDABOT_ALERTS = '/dependabot/alerts'

def run(config: dict):
    result = []

    url = config['base'] + ENDPOINT_DEPENDABOT_ALERTS

    params = config.get("params", "")
    response = requests.get(url, params=params, headers = config.get('headers'), verify = config.get('verify', False))
    response = response.json()

    for res in response:
        newresponse = { 'type': 'dependabot_sca', 'title': res["security_advisory"]["summary"], 'response': {}}
        newresponse['response'] = res
        newresponse = util.flatten(newresponse)
        result.append(newresponse)

    return result