#!/usr/bin/python3
from ncclient import manager
import xmltodict
import xml.dom.minidom

# read xml file
X_File = xml.dom.minidom.parse("run-config.xml")

hostname = X_File.getElementsByTagName("hostname")
print(hostname[0].firstChild.nodeValue)