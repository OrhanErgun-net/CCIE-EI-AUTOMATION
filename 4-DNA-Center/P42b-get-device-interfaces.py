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

# # URL for device interfaces
# URL_Device_Intf = f"/dna/intent/api/v1/interface/network-device/{Selected_ID}"
# Res_Device_Intf = requests.get(url=f"{DNAC}{URL_Device_Intf}", headers=Headers, verify=False).json()
# print(json.dumps(Res_Device_Intf, indent=2))

# with open('Device_'+ Selected_IP +'_interfaces.json', 'w') as f:
#     json.dump(Res_Device_Intf['response'], f, indent=2)

# ######### Pretty Print ########

# print("{:<30}  {:<30}  {:<40}".format('Port Name','Port Type','Interface ID'))
# for Intf in Res_Device_Intf['response']:
#     print("{:<30}  {:<30}  {:<40}".format(Intf['portName'],Intf['portType'],Intf['id']))