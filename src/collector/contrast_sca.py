import requests
import util
import json

ENDPOINT_APPLICATIONS = '/applications'
ENDPOINT_APPLICATION_LIBRARY = '/{contrastAppId}/libraries/filter'

def run(config: dict, itemid: str):
    result = []

    contrastAppIds = getContrastAppIds(config, itemid)

    for id in contrastAppIds:
        url = config['base'] + ENDPOINT_APPLICATIONS + ENDPOINT_APPLICATION_LIBRARY.format(contrastAppId=id)
        url = url + config['params']

        response = requests.get(url, headers = config.get('headers'), verify = config.get('verify', False))
        response = response.json()

        for res in response['libraries']:
            newresponse = { 'type': 'contrast_lib', 'appId': itemid, 'contrastAppId': id, 'libraries': {}}
            newresponse['libraries']['classes_used'] = res['classes_used']
            newresponse = util.flatten(newresponse)
            result.append(newresponse)

    return result




def getContrastAppIds(config: dict, itemid: str) -> list:
    allAppIds = []

    base = config['base']
    url = base + ENDPOINT_APPLICATIONS

    response = requests.get(url, headers = config.get('headers'), verify = config.get('verify', False))
    response = response.json()

    for d in response["applications"]:
        if d["short_name"] == itemid:
            allAppIds.append(d["app_id"])

    return allAppIds