DEFAULT_MISSING = { "result": "missing" }
MAX_PRIO = 1024
MIN_COUNT = 1

def run(config: dict, items: list):
    items = [ item for item in items if item != None ]

    countmissing = config.get('count', MIN_COUNT) - len(items)
    if countmissing > 0:
        items += [ config.get('missing', DEFAULT_MISSING).copy() ] * countmissing

    items.sort(key = lambda x: x.get('prio', MAX_PRIO))

    return items[0]