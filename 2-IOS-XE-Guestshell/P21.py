from cli import *
import re

COMD_1=(execute('show run'))
################################

HostName = re.findall(r'hostname\s+(\S*)', COMD_1)[0]
print (HostName)


##################################


for line in COMD_1.splitlines():
    if line.startswith('hostname'):
        HostName = line.split()[1]
print (HostName)
