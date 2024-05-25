import requests
import util
import json

ENDPOINT_APPLICATIONS = '/applications'
ENDPOINT_APPLICATION_VULNERABILITY_FILTERING = '/traces/{contrastAppId}/filter'

def run(config: dict, itemid: str):
    result = []

    contrastAppIds = getContrastAppIds(config, itemid)

    for id in contrastAppIds:
        url = config['base'] + ENDPOINT_APPLICATION_VULNERABILITY_FILTERING.format(contrastAppId=id)

        response = requests.get(url, headers = config.get('headers'), verify = config.get('verify', False))
        response = response.json()

        for res in response['traces']:
            newresponse = { 'type': 'contrast_codeVuln', 'appId': itemid, 'contrastAppId': id, 'traces': {}}
            newresponse['traces']['severity'] = res['severity']
            newresponse['traces']['status'] = res['status']
            newresponse['traces']['instance_uuid'] = res['instance_uuid']
            newresponse['traces']['sub_title'] = res['sub_title']
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