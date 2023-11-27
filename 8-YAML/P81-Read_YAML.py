#!/usr/bin/python3
import yaml

# open and read yaml file
with open("Creds.yaml") as f:
    Yaml_file=yaml.safe_load(f)
    
# print yaml output
print(Yaml_file)