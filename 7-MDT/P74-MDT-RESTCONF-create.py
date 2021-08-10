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

URL_Config = f"https://{Host_IP}/restconf/data/Cisco-IOS-XE-mdt-cfg:mdt-config-data"

PL = json.dumps({
  "Cisco-IOS-XE-mdt-cfg:mdt-config-data": {
    "mdt-subscription": [
      {
        "subscription-id": 360,
        "base": {
          "stream": "yang-push",
          "encoding": "encode-kvgpb",
          "source-address": "192.168.96.121",
          "no-synch-on-start": False,
          "xpath": "/cdp-ios-xe-oper:cdp-neighbor-details/cdp-neighbor-detail"
        },
        "mdt-receivers": [
          {
            "address": "192.168.96.80",
            "port": 57000,
            "protocol": "grpc-tcp"
          }
        ]
      }
    ]
  }
})

RES_Config = requests.put(URL_Config,auth = (UserName, PassWord),
                        verify = False,headers = Headers, data = PL)

print(RES_Config)