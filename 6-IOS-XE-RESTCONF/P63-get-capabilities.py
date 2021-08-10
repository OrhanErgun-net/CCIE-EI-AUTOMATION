import urllib3, requests, json
from bs4 import BeautifulSoup

# Disable SSL Warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Host Creds
Host_IP = "192.168.96.121"
UserName = "cisco"
PassWord = "cisco"

URL = f"https://{Host_IP}/restconf/data/netconf-state/capabilities"

RES = requests.get(URL,
                        auth = (UserName, PassWord),
                        verify = False,
                        headers = {
                                 'Accept': 'application/yang-data+json',
                                 'Content-Type': 'application/yang-data+json'}
                       )


print(RES.text)

# Print in Bytes
# print(RES.content)


# Print as JSON
# print(RES.json())


# Print Pretty JSON
# print(json.dumps(RES.json(), indent=4))





