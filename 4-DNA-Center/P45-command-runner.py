#!/usr/bin/python3
import urllib3, requests, json, sys, time

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
Res_Devices = requests.get(url=f"{DNAC}{URL_Devices}",  headers=Headers, verify=False).json()

# print(json.dumps(Res_Devices, indent=2))

# Select device ID by device IP
Selected_IP = '172.30.255.3'
for device in Res_Devices['response']:
    if device['managementIpAddress'] == Selected_IP:
        Selected_ID = device['id']

# print (Selected_ID)

########### end of selection ###########
# Build payload with required readonly commands , Sending it to target device (ID)
PL= json.dumps({
  "name": "show ver",
  "commands": ["show ver | inc RELEASE"],
  "deviceUuids": [Selected_ID]
})

# URL for Command Runner
URL_COMD_Run = "/api/v1/network-device-poller/cli/read-request"
Res_COMD_Run = requests.post(url=f"{DNAC}{URL_COMD_Run}",  headers=Headers, data=PL, verify=False).json()
print (Res_COMD_Run['response'])


# # URL for Task status
# URL_Task_ID=(Res_COMD_Run['response']['url'])
# # Res_Task = requests.get(url=f"{DNAC}{URL_Task_ID}",  headers=Headers, verify=False).json()
# # print (Res_Task['response'])

# # For loop waiting for File ID to be generated
# for i in range(6):
#     time.sleep(1)
#     Res_Task = requests.get(url=f"{DNAC}{URL_Task_ID}",  headers=Headers, verify=False).json()

#     # Extract File ID
#     if "fileId" in Res_Task['response']['progress']:
#         File_ID=json.loads(Res_Task['response']['progress'])['fileId']
#         break
#     else:
#         print("Waiting for File ID")

# # Exiting the script if no File ID found
# if not File_ID:
#     print("No File ID")
#     sys.exit(0)


# # URL for File "Command Runner resault"
# URL_File_ID=f"/api/v1/file/{File_ID}"
# Res_File = requests.get(url=f"{DNAC}{URL_File_ID}",  headers=Headers, verify=False).json()
# # Parsing the output file
# print (Res_File[0]['commandResponses']['SUCCESS']['show ver | inc RELEASE'])