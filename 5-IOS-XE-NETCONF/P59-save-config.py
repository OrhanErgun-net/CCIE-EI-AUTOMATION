#!/usr/bin/python3
from ncclient import manager, xml_
import xmltodict
import xml.dom.minidom

m = manager.connect(host='192.168.96.121', port=830, username='cisco',
                    password='cisco', device_params={'name': 'csr'})

 
# Create RPC Payload
Save_PL = '<cisco-ia:save-config xmlns:cisco-ia="http://cisco.com/yang/cisco-ia"/>'

# Send RPC 
Save_RPC = m.dispatch(xml_.to_ele(Save_PL))
print(Save_RPC)





