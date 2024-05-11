import util
import json

if __name__ == '__main__':
    import sys
    param = sys.argv[1]
    config = util.loadConfig(param)
    print(json.dumps(config, indent = 2))