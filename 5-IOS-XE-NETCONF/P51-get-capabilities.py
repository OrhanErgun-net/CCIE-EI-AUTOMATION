#!/usr/bin/python3
from ncclient import manager
import xmltodict
import xml.dom.minidom

m = manager.connect(host='192.168.96.121', port=830, username='cisco',
                    password='cisco', device_params={'name': 'csr'})


# for c in m.server_capabilities:
#     print(c)




with open("capabilities.txt", 'w') as f:
    for c in m.server_capabilities:
        f.write(c)
        f.write("\n"+80*"-"+"\n")



######## rpc-relpy ID
# schema = m.get_schema('ietf-interfaces')
# print (schema)
# with open("schema-ietf-interfaces.xml", 'w') as f:
#     f.write(str(schema))