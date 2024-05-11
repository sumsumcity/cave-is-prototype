import util
import json

DEFAULT_ERROR = { 'result': 'error' }

def main(config: dict):

    results = []
    for itemid, itemconfig in config['items'].items():
        for metricid, metrictemplate in config['metrics'].items():
            stage = 'init'
            stageresult = {}
            try:
                metricconfig = metrictemplate.copy()
                metricconfig.update(itemconfig.get(metricid, {}))

                stage = 'collector'
                stageconfig = metricconfig[stage]
                stageresult = collect(stageconfig)

                stage = 'validator'
                stageconfig = metricconfig.get(stage, [])
                stageresult = [ validate(stageconfig, e) for e in stageresult ]

                stage = 'aggregator'
                stageconfig = metricconfig.get(stage, {})
                stageresult = aggregate(stageconfig, stageresult)
            except Exception as e:
                stageresult.update(DEFAULT_ERROR)
                stageresult['title'] = f'{type(e).__name__}: {e}'

            stageresult['item'] = itemid
            stageresult['metric'] = metricid
            results.append(stageresult)

    serialize(config['serializer'], results)

def collect(config: dict):
    result = {}
    if config['type'] == 'generator':
        #result = collector.generator.run(config)
        print("generator collector")
    if config['type'] == 'http':
        #result = collector.http.run(config)
        print("http collector")
    if config['type'] == 'jira':
        #result = collector.jira.run(config)
        print("jira collector")
    return result

 

def validate(config: list, element: dict):
    result = element.copy()
    #result.update(validator.document.run(config, element))
    print("validator")
    return result

 

def aggregate(config: dict, validations: list):
    #result = aggregator.sorter.run(config, validations)$
    result=[]
    print("aggregator")
    return result

 

def serialize(config: dict, results: list):
    if config['type'] == 'json':
        #serializer.json.run(config, results)
        print("json serializer")
    if config['type'] == 'mysql':
        #serializer.mysql.run(config, results)
        print("mysql serializer")


if __name__ == '__main__':
    import sys
    param = sys.argv[1]
    config = util.loadConfig(param)

    print(json.dumps(config, indent = 2))
    #main(config)