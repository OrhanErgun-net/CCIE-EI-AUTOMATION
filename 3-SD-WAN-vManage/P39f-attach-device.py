import urllib3, requests, json, sys

# Disable SSL Warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Create verification function for authrntication
def Verf_Res(Res):
    if b'<html>' in Res.content:
        print("Response Test Failed")
        sys.exit(0)

# Create verification function for resonse data
def Verf_Data(Res):
    # Check entire response 
    if not isinstance(Res,dict):
        print("Main Response Not Dict")
        sys.exit(0)
    # Check if there is a data
    elif "data" not in Res:
        print("Data Part does not exist")
        sys.exit(0)
    elif not Res["data"]:
        print("Data Part is empty")
        sys.exit(0)


# Host Creds
UserName = "admin"
PassWord = "C1sco12345"
Headers={'Accept': 'application/json',
        'Content-Type': 'application/json'}

# URL for auth, key=j
URL_Login = "https://10.10.20.90/j_security_check"

# PayLoad with creds
Body_Login = {"j_username": UserName,"j_password": PassWord}

# keeps connection up with same login creds
Sess_Login = requests.session()

# Login using Post
Res_Login = Sess_Login.post(url=URL_Login, data=Body_Login, verify=False)

# Use the verification function on the returned response
Verf_Res(Res_Login)

# URL for Token
URL_Token = "https://10.10.20.90/dataservice/client/token"

# Get Token
Res_Token = Sess_Login.get(url=URL_Token)

# Use the verification function on the returned Token
Verf_Res(Res_Token)

Sess_Login.headers['X-XSRF-TOKEN']=Res_Token.text


##################  end of auth ##################

# Find Template ID >>OE_template
URL_Templates = 'https://10.10.20.90/dataservice/template/device'

Res_Templates = Sess_Login.get(url=URL_Templates, verify=False).json()

Verf_Data(Res_Templates)

for item in Res_Templates['data']:
    if "OE_template" in item['templateName']:
        print (item['templateId'])

Template_ID=(item['templateId'])

##################################################################

# Find Device UUID >> site3-vedge01
URL_uDevice = 'https://10.10.20.90/dataservice/device'

Res_uDevice = Sess_Login.get(url=URL_uDevice, verify=False).json()

Verf_Data(Res_uDevice)

# print (json.dumps(Res_uDevice, indent=2))

for item in Res_uDevice['data']:
    if 'site3-vedge01' in item['host-name']:
        print (item['uuid'])
Device_ID=(item['uuid'])

##################################################################

# URL for attaching Template to Devices
URL_Attach = 'https://10.10.20.90/dataservice/template/device/config/input'

PL = json.dumps({
   "templateId":Template_ID,
   "deviceIds":[
      Device_ID
   ],
   "isEdited":False,
   "isMasterEdited":False
})


Res_Attach = Sess_Login.post(url=URL_Attach, data=PL, headers=Headers, verify=False).json()
print (json.dumps(Res_Attach['data'], indent=2))

