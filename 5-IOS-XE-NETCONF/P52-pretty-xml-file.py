#!/usr/bin/python3
from ncclient import manager
import xmltodict
import xml.dom.minidom

m = manager.connect(host='192.168.96.121', port=830, username='cisco',
                    password='cisco', device_params={'name': 'csr'})



c = m.get_config(source='running').data_xml

# with open("run-config.xml", 'w') as f:
#     f.write(c)

############
# XD = xml.dom.minidom.parseString(str(c))
# with open("run-config-pretty.xml", 'w') as f:
#     f.write(XD.toprettyxml( indent = "  " ))


############

Pretty_filter = '''
                <filter>
                    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
                    </native>
                </filter>
                '''

XD = xml.dom.minidom.parseString( str( m.get_config('running', Pretty_filter)))
print(XD.toprettyxml( indent = "  " ))
with open("run-config-pretty-2.xml", 'w') as f:
    f.write(XD.toprettyxml( indent = "  " ))