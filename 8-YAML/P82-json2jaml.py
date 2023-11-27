#!/usr/bin/python3
import yaml,json

# open and read json file
with open("output-01.json") as f:
    json_file=json.load(f)
    
# print normal json output
print(json.dumps(json_file))

# print normal json output with indention
# print(json.dumps(json_file,indent=2))

# print converted json to yaml data
# print (yaml.dump(json_file))