#!/usr/bin/python3
import yaml
from jinja2 import Template

# Open and read Data file
with open('Data.yaml') as f:
    Data_file = yaml.safe_load(f)    

# Open and read Template file
with open('Template.jinja') as f:
    Template_file = Template(f.read())

# Open and write Rendered file
with open("Rendered_conf.ios", 'w') as f:
    f.write(Template_file.render(Data_file))