import urllib3, requests, json
from bs4 import BeautifulSoup

# Disable SSL Warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Host Creds
Host_IP = "192.168.96.121"
UserName = "cisco"
PassWord = "cisco"

URL = f"https://{Host_IP}/.well-known/host-meta"

RES = requests.get(URL,
                        auth = (UserName, PassWord),
                        verify = False)

print(RES)


# Print content if successful
# if RES.status_code == 200:
#     print(RES.text)