import util
import json
import collector.generator
import collector.http
import collector.jira
import serializer.json
import serializer.mysql
import validator.document
import aggregator.sorter

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
                stageresult['title'] = f'{type(e).__name__} in {stage} stage: {e}'

            stageresult['item'] = itemid
            stageresult['metric'] = metricid
            results.append(stageresult)

    serialize(config['serializer'], results)

def collect(config: dict):
    result = {}
    if config['type'] == 'generator':
        result = collector.generator.run(config)
    if config['type'] == 'http':
        result = collector.http.run(config)
    if config['type'] == 'jira':
        result = collector.jira.run(config)
    if config['type'] == 'contrast_iast':
        result = collector.contrast_iast.run(config)
    return result

 

def validate(config: list, element: dict):
    result = element.copy()
    result.update(validator.document.run(config, element))
    return result

 

def aggregate(config: dict, validations: list):
    result = aggregator.sorter.run(config, validations)
    return result

 

def serialize(config: dict, results: list):
    if config['type'] == 'json':
        serializer.json.run(config, results)
    if config['type'] == 'mysql':
        serializer.mysql.run(config, results)


if __name__ == '__main__':
    import sys
    param = sys.argv[1]
    config = util.loadConfig(param)

    #print(json.dumps(config, indent = 2))
    main(config)