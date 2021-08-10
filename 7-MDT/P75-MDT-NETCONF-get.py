#!/usr/bin/python3
import xmltodict
import xml.dom.minidom
from lxml.etree import fromstring
from ncclient import manager

m = manager.connect(host='192.168.96.121', port=830, username='cisco',
                    password='cisco', device_params={'name': 'csr'})

Filter_X="/mdt-oper-data/mdt-subscriptions"
netconf_reply = m.get(filter=("xpath",Filter_X))
# print (netconf_reply)
XD = xml.dom.minidom.parseString( str(netconf_reply))
print(XD.toprettyxml( indent = "  " ))

# Print specific value
# SubID = XD.getElementsByTagName("subscription-id")
# print(SubID[0].firstChild.nodeValue)

# Loop to print all values
# for item in range(0, len(SubID)):
#     print (SubID[item].firstChild.nodeValue)

