#!/usr/bin/python3
from cli import *
from ntc_templates.parse import parse_output

COMD_1=(execute('show interfaces'))
PARSE_1 = parse_output(platform="cisco_ios", command="show interfaces", data=COMD_1)
# print (PARSE_1)


for item in PARSE_1:
    print (item['interface']+ "   "+item['mtu'])
    print('{:<20}  {:^16}'.format(item['interface'], item['mtu']))
    if int(item['mtu']) == 1500:
        print('{:<20}  {:^16}'.format(item['interface'], item['mtu']))
