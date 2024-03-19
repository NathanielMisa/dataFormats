import yaml

with open("devices.yaml") as f:
    yamlDict = yaml.safe_load(f)

print(yamlDict)