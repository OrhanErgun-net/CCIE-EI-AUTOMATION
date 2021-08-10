import urllib3, requests, json
from bs4 import BeautifulSoup

# Disable SSL Warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Host Creds
Host_IP = "192.168.96.121"
UserName = "cisco"
PassWord = "cisco"

URL = f"https://{Host_IP}/restconf/data/Cisco-IOS-XE-native:native/hostname/"

RES = requests.get(URL,
                        auth = (UserName, PassWord),
                        verify = False,
                        headers = {
                                 'Accept': 'application/yang-data+json',
                                 'Content-Type': 'application/yang-data+json'}
                       )


# Convert and print as JSON
RES_J=(RES.json())
print (RES_J)

# print (list(RES_J.values())[0])