#!/usr/bin/python3
from cli import *
from ntc_templates.parse import parse_output
from datetime import datetime
import os

date = datetime.now().strftime("%Y_%m_%d-%I:%M:%S_%p")
FileName=(f"MTU_{date}.txt")

os.chdir("/bootflash/guest-share/date/")


COMD_1=(execute('show interfaces'))
PARSE_1 = parse_output(platform="cisco_ios", command="show interfaces", data=COMD_1)
# print (PARSE_1)

with open(FileName, 'a') as f:
    for item in PARSE_1:
        f.write(('{:<20}  {:^16}'.format(item['interface'], item['mtu']))+"\n")

executep('more flash:guest-share/date/'+FileName)




