#!/usr/bin/python3
import xmltodict
import xml.dom.minidom
from lxml.etree import fromstring
from ncclient import manager

m = manager.connect(host='192.168.96.121', port=830, username='cisco',
                    password='cisco', device_params={'name': 'csr'})

Config_Set  = """
<config>
    <mdt-config-data xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-mdt-cfg">
            <mdt-subscription>
                    <subscription-id>360</subscription-id>
                    <base>
                            <stream>yang-push</stream>
                            <encoding>encode-kvgpb</encoding>
                            <source-address>192.168.96.121</source-address>
                            <no-synch-on-start>false</no-synch-on-start>
                            <xpath>/cdp-ios-xe-oper:cdp-neighbor-details/cdp-neighbor-detail</xpath>
                    </base>
                    <mdt-receivers>
                            <address>192.168.96.80</address>
                            <port>57000</port>
                            <protocol>grpc-tcp</protocol>
                    </mdt-receivers>
            </mdt-subscription>
    </mdt-config-data>
</config>
"""


NETCONF_reply = m.edit_config(Config_Set, target="running")
print(NETCONF_reply)
