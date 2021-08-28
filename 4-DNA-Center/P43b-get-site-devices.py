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

# URL for listing Sites
URL_Sites = "/dna/intent/api/v1/site"

Res_Sites = requests.get(url=f"{DNAC}{URL_Sites}", headers=Headers, verify=False).json()

# print(json.dumps(Res_Sites['response'], indent=2))

# Select Site ID by Site Name
# Selected_Name = 'BLD01'
Selected_Name = 'Ankara'
for site in Res_Sites['response']:
    if site['name'] == Selected_Name:
        Selected_ID = site['id']

print (Selected_ID)

# URL for site devices
URL_Site_Devices = f"/dna/intent/api/v1/membership/{Selected_ID}"
Res_Site_Devices = requests.get(url=f"{DNAC}{URL_Site_Devices}", headers=Headers, verify=False).json()
print(json.dumps(Res_Site_Devices['device'][0]['response'], indent=2))

######## Pretty Print ########

# print("{:<20}  {:<16}  {:<16}".format('Host Name','MGMT IP','Device ID'))
# for device in Res_Site_Devices['device'][0]['response']:
#     print("{:<20}  {:<16}  {:<16}".format(device['hostname'],device['managementIpAddress'],device['instanceUuid']))