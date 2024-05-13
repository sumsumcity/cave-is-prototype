import datetime
import env
import re
import requests

DATE_RFC2822 = '%a, %d %b %Y %H:%M:%S %Z'
DATE_ISO6801 = '%Y-%m-%d'

def run(config: dict):
    url = config['url']
    now = env.now()

    response = requests.get(url, headers = config.get('headers'), verify = config.get('verify', True))

    if response.status_code == 404:
        return []

    result = { 'type': 'document', 'title': url, 'date': now, 'content': response.text }

    if response.status_code != 200:
        result['title'] = f'{response.status_code} {response.reason}'
        result['date'] = datetime.datetime(1970, 1, 1)
        result['content'] = ''

    if 'content' in result:
        match = re.search('<title>([^<>]+)</title>', result['content'])
        if match and match.group(1):
            result['title'] = match.group(1)

    if 'Last-Modified' in response.headers:
        result['date'] = datetime.datetime.strptime(response.headers['Last-Modified'], DATE_RFC2822)

    if 'dateregex' in config:
        match = re.search(config['dateregex'], result['content'])
        if match and match.group(1):
            result['date'] = datetime.datetime.strptime(match.group(1), config['dateformat'])

    result['date'] = result['date'].strftime(DATE_ISO6801)

    return [ result ]

 

 

 

 
