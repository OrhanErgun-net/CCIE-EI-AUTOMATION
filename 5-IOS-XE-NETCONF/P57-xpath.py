#!/usr/bin/python3
from ncclient import manager
import xmltodict
import xml.dom.minidom

m = manager.connect(host='192.168.96.121', port=830, username='cisco',
                    password='cisco', device_params={'name': 'csr'})


Filter_X="/interfaces-state/interface[name='GigabitEthernet1']/phys-address"
netconf_reply = m.get(filter=("xpath",Filter_X))

# XD = xml.dom.minidom.parseString( str(netconf_reply))
# print(XD.toprettyxml( indent = "  " ))

Intf_Name= xmltodict.parse(netconf_reply.xml)["rpc-reply"]["data"]["interfaces-state"]["interface"]["name"]
Intf_MAC = xmltodict.parse(netconf_reply.xml)["rpc-reply"]["data"]["interfaces-state"]["interface"]["phys-address"]



print("\nInterface: {}".format(Intf_Name))
print("  Packets Output: {}".format(Intf_MAC))

