import urllib3, requests, json, sys

# Disable SSL Warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

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

# print (Res_Login)

# Verifing Part
if b'<html>' in Res_Login.content:
    print("Login Failed")
    print(Res_Login.text)
    sys.exit(0)
else:
    print("Login Successful")
