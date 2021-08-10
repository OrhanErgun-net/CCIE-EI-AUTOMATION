#!/usr/bin/python3
import xmltodict
# Open the sample xml file and read it into variable
with open ("show_ip_int_brief.xml") as f:
    xml_example = f.read()
# Print the raw XML data
# print(xml_example)
# Parse the XML into a Python dictionary
xml_dict = xmltodict.parse(xml_example)
# print (xml_dict)

# Save the interface name into a variable using XML nodes as keys
int_name = xml_dict["ShowIpInterfaceBrief"]["IPInterfaces"]["entry"]
# Print the interface name
print(int_name)

