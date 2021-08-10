#!/usr/bin/python3
from ncclient import manager
import xmltodict
import xml.dom.minidom

m = manager.connect(host='192.168.96.121', port=830, username='cisco',
                    password='cisco', device_params={'name': 'csr'})

Config_Set = '''
<config>
  <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
	<interface>
	  <name>GigabitEthernet3</name>
	  <description>NETCONF WAS HERE</description>
	  <type xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">ianaift:ethernetCsmacd</type>
	  <enabled>true</enabled>
	  <ipv4 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip">
		<address>
		  <ip>172.16.3.1</ip>
		  <netmask>255.255.255.0</netmask>
		</address>
	  </ipv4>
	</interface>
  </interfaces>
</config>
'''

XD = m.edit_config(Config_Set, target="running")
print(XD)



