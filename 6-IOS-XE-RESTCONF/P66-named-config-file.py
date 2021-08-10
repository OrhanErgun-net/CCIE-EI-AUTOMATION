import urllib3, requests, json
from bs4 import BeautifulSoup

# Disable SSL Warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Host Creds
Host_IP = "192.168.96.121"
UserName = "cisco"
PassWord = "cisco"
Headers={'Accept': 'application/yang-data+json',
        'Content-Type': 'application/yang-data+json'}

URL_HostName = f"https://{Host_IP}/restconf/data/Cisco-IOS-XE-native:native/hostname/"
URL_Config = f"https://{Host_IP}/restconf/data/Cisco-IOS-XE-native:native/"

RES_HostName = requests.get(URL_HostName,auth = (UserName, PassWord),
                        verify = False,headers = Headers).json()

RES_Config = requests.get(URL_Config,auth = (UserName, PassWord),
                        verify = False,headers = Headers).json()

# Check Response Data Type
# print (type(RES_HostName))

HostName=(list(RES_HostName.values())[0])

with open(f'{HostName}.json', 'w', encoding='utf-8') as f:
    json.dump(RES_Config, f, ensure_ascii=False, indent=2)