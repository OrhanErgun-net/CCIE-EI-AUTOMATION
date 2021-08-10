from cli import *
import re,time
start = time.time()
COMD_1=(execute('show run'))

HostName = re.findall(r'hostname\s+(\S*)', COMD_1)[0]
print (HostName)

end = time.time()
print(end - start)

##################################
print (50*'#')

start = time.time()
COMD_1=(execute('show run'))
for line in COMD_1.splitlines():
    if line.startswith('hostname'):
        HostName = line.split()[1]
print (HostName)
end = time.time()
print(end - start)