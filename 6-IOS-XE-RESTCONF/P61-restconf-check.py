import urllib3, requests, json

# Host Creds
Host_IP = "192.168.96.121"
UserName = "cisco"
PassWord = "cisco"

URL = f"https://{Host_IP}/.well-known/host-meta"

RES = requests.get(URL,
                        auth = (UserName, PassWord),
                        verify = False)

print(RES)
