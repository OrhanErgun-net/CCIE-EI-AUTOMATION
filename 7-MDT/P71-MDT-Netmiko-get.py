#!/usr/bin/python3
from netmiko import ConnectHandler

# Define dictionary
IP_dic = {'device_type': 'cisco_ios', 'ip': '192.168.96.121', 'username': 'cisco', 'password': 'cisco'}

net_connect = ConnectHandler(**IP_dic)

# Send show command
output = net_connect.send_command("show run | sec tel")
net_connect.disconnect()

print (output)