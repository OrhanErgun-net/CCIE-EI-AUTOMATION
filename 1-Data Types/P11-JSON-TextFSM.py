#!/usr/bin/python3
from netmiko import ConnectHandler
import json

# Define dictionary
IP_dic = {'device_type': 'cisco_ios', 'ip': '192.168.96.121', 'username': 'cisco', 'password': 'cisco'}

net_connect = ConnectHandler(**IP_dic)

# Send show command with textFSM filter to parse output
output = net_connect.send_command("show vlan brief ", use_textfsm=True)
net_connect.disconnect()

# textFSM parsed the output variable type to be dictionary 
# print (output)

# Print all output using for loop
for item in output:
    # print (item)
    if int(item['vlan_id']) < 1002 :
        print (item)

with open("output-01.json", "w") as outfile: 
    json.dump(output, outfile)