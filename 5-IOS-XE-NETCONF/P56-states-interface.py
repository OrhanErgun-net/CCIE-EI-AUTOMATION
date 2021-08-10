#!/usr/bin/python3
from ncclient import manager
import xmltodict
import xml.dom.minidom

m = manager.connect(host='192.168.96.121', port=830, username='cisco',
                    password='cisco', device_params={'name': 'csr'})


Pretty_filter = '''
                <filter>
                <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
                    <interface>
                    <name>GigabitEthernet1</name>
                    </interface>
                </interfaces>
                <interfaces-state xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
                    <interface>
                    <name>GigabitEthernet1</name>
                    </interface>
                </interfaces-state>
                </filter>
                '''

c = m.get(Pretty_filter)

XD = xml.dom.minidom.parseString( str(c))
print(XD.toprettyxml( indent = "  " ))
with open("Interface-status.xml", 'w') as f:
    f.write(XD.toprettyxml( indent = "  " ))

# Parse xml into Config and Info
Intf = xmltodict.parse(c.xml)["rpc-reply"]["data"]
Intf_Config = Intf["interfaces"]["interface"]
Intf_Info = Intf["interfaces-state"]["interface"]

# Extract Interface details
print("\nInterface: {}".format(Intf_Config["name"]["#text"]))
print("  Description: {}".format(Intf_Config["description"]))
print("  Type: {}".format(Intf_Config["type"]["#text"]))
print("  MAC Address: {}".format(Intf_Info["phys-address"]))
print("  Packets Input: {}".format(Intf_Info["statistics"]["in-unicast-pkts"]))
print("  Packets Output: {}".format(Intf_Info["statistics"]["out-unicast-pkts"]))

