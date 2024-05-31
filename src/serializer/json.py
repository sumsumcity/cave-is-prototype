import json

def run(config: dict, data: list):
    print(config)
    with open(config["output"], "w") as fp:
        for item in data:
            runonce(fp, item)

def runonce(fp, item: dict):
    out = {}
    for k in ["item", "metric", "result", "description"]:
        out[k] = item[k]

    json.dump(out, fp)
    print('', file = fp)