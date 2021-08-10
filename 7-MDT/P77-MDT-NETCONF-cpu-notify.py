#!/usr/bin/python3
import xmltodict
from lxml.etree import fromstring
from ncclient import manager


m = manager.connect(host='192.168.96.121', port=830, username='cisco',
                    password='cisco', device_params={'name': 'csr'})

Xpath = "/process-cpu-ios-xe-oper:cpu-usage/cpu-utilization/five-seconds"
RPC = f'''
    <establish-subscription xmlns='urn:ietf:params:xml:ns:yang:ietf-event-notifications' xmlns:yp='urn:ietf:params:xml:ns:yang:ietf-yang-push'>
        <stream>yp:yang-push</stream>
        <yp:xpath-filter>{Xpath}</yp:xpath-filter>
        <yp:period>500</yp:period>
    </establish-subscription>
'''

# dispatch is used with RPC commands
RPC_Res = m.dispatch(fromstring(RPC))

while True:

    T_Notification = xmltodict.parse(m.take_notification().notification_xml)
    # print(T_Notification)
    print(f" {T_Notification['notification']['push-update']['datastore-contents-xml']['cpu-usage']['cpu-utilization']['five-seconds']}% CPU")
    