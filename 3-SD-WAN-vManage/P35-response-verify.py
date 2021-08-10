import urllib3, requests, json, sys

# Disable SSL Warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Create verification function
def Verf_Res(Res):
    if b'<html>' in Res.content:
        print("Response Test Failed")
        sys.exit(0)

# Host Creds
UserName = "devnetuser"
PassWord = "RG!_Yw919_83"

# URL for auth, key=j
URL_Login = "https://sandbox-sdwan-1.cisco.com/j_security_check"

# PayLoad with creds
Body_Login = {"j_username": UserName,"j_password": PassWord}

# keeps connection up with same login creds
Sess_Login = requests.session()

# Login using Post
Res_Login = Sess_Login.post(url=URL_Login, data=Body_Login, verify=False)

# Use the verification function on the returned response
Verf_Res(Res_Login)

# URL for Token
URL_Token = "https://sandbox-sdwan-1.cisco.com/dataservice/client/token"

# Get Token
Res_Token = Sess_Login.get(url=URL_Token)

# Use the verification function on the returned Token
Verf_Res(Res_Token)

# print (Res_Token)
# print (Res_Token.text)
# print (Sess_Login.headers)

# Sess_Login.headers['X-XSRF-TOKEN']=Res_Token.text
# print (Sess_Login.headers)