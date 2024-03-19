import yaml
import json

with open("devices.json") as f:
    openedFile = f.read()
    jsonDict = json.loads(openedFile)

with open("devices.yaml", "w") as f:
    yaml.dump(jsonDict, f, default_flow_style=False )