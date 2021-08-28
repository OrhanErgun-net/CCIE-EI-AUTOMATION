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
print (Res_Login.json()['Token'])

# Update session headers with the token
Headers['x-auth-token']=Res_Login.json()['Token']
# print (Headers)