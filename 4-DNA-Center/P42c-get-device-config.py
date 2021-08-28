#!/usr/bin/python3
import urllib3, requests, json, sys

# Disable SSL Warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Create verification function for authrntication
def Verf_Auth(Res):
    if b"Token" not in Res.content:
        print("Authentication Test Failed")
        sys.exit(0)

# Auth Creds
#Auth=(UserName,PassWord)
Auth=("admin","P@ssw0rd")

# Headers
Headers={'Accept': 'application/json',
        'Content-Type': 'application/json'}

# Main URL
DNAC = "https://192.168.222.111"

# URL for auth login and token
URL_Login = "/dna/system/api/v1/auth/token"

# Login using Post
Res_Login = requests.post(url=f"{DNAC}{URL_Login}", auth=Auth, headers=Headers, verify=False)

Verf_Auth(Res_Login)

# Extract Token only
# print (Res_Login.json()['Token'])

# Update session headers with the token
Headers['x-auth-token']=Res_Login.json()['Token']
# print (Headers)

##################  end of auth ##################

# URL for listing devices 
URL_Devices = "/dna/intent/api/v1/network-device"
Res_Devices = requests.get(url=f"{DNAC}{URL_Devices}", headers=Headers, verify=False).json()

# Select device ID by device IP
Selected_IP = '172.30.255.3'
for device in Res_Devices['response']:
    if device['managementIpAddress'] == Selected_IP:
        Selected_ID = device['id']

print (Selected_ID)

# URL for device configs
URL_Device_Conf = f"/dna/intent/api/v1/network-device/{Selected_ID}/config"
Res_Device_Conf = requests.get(url=f"{DNAC}{URL_Device_Conf}", headers=Headers, verify=False).json()
print (Res_Device_Conf['response'])

with open('Device_'+ Selected_IP +'_Config.txt', 'w') as f:
    f.write(Res_Device_Conf['response'])

