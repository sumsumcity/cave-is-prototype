from src import util
import json

cfg = util.loadConfig("example/config.json")

print(json.dumps(cfg, indent = 2))