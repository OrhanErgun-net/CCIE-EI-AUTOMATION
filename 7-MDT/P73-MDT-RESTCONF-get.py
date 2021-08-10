#!/usr/bin/python3
import urllib3, requests, json

# Disable SSL Warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Host Creds
Host_IP = "192.168.96.121"
UserName = "cisco"
PassWord = "cisco"
Headers={'Accept': 'application/yang-data+json',
        'Content-Type': 'application/yang-data+json'}

URL = f"https://{Host_IP}/restconf/data/Cisco-IOS-XE-mdt-cfg:mdt-config-data"

RES = requests.get(URL,auth = (UserName, PassWord),verify = False, headers = Headers).json()

# Convert and print as JSON
print (json.dumps(RES, indent=2))
