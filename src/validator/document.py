import env
import re
import isodate

DEFAULT_FAIL = { "result": "fail" }

def run(config: list, document: dict):
    for result in config:
        if check(result, document):
            return result

    return DEFAULT_FAIL

def check(conditions: dict, doc: dict):
    result = True
    now = env.now().date()

    for field, condition in conditions.items():

        if field.startswith('str:'):
            value = doc.get(field[4:], '')
            result = result and re.search(condition, value)

        if field.startswith('date:'):
            condition = isodate.parse_duration(condition)
            value = doc.get(field[5:], '0001-01-01')
            value = isodate.parse_date(value[0:10])
            result = result and now - condition < value

    return result