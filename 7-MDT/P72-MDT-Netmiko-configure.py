#!/usr/bin/python3
from netmiko import ConnectHandler

with open ("MDT-config-file.txt",'r') as f:
    Configs = f.readlines()
print (Configs)

# Define dictionary
IP_dic = {'device_type': 'cisco_ios', 'ip': '192.168.96.121', 'username': 'cisco', 'password': 'cisco'}

net_connect = ConnectHandler(**IP_dic)

# Send Configurations
output = net_connect.send_config_set(Configs)
net_connect.disconnect()

print (output)