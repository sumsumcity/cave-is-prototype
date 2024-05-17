import requests
import util
import json

ENDPOINT_SEARCH = '/rest/api/2/search'

def run(config: dict):
    base = config['base']

    url = base + ENDPOINT_SEARCH
    params = { 'jql': config['jql'], 'expand': 'names' }

    response = requests.get(url, params = params, headers = config.get('headers'), verify = config.get('verify', False))
    response = response.json()

    fields = response['names']

    result = []

    for issue in response['issues']:
        newissue = { 'type': 'jira', 'title': '', 'issue': {} }
        newissue['title'] = issue["fields"]['summary']
        newissue['issue']['id'] = issue['id']
        newissue['issue']['key'] = issue['key']

        for k, v in issue['fields'].items():
            if k.startswith('customfield'):
                if not v:
                    continue
                k = fields[k]

            newissue['issue'][k] = v

        newissue = util.flatten(newissue)
        result.append(newissue)

    return result