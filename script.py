import requests
AUTH_URL = "https://mbn-provider.authentication.eu12.hana.ondemand.com/oauth/token"
TRANSPORT_URL = "https://interview-demo-transport-backend.cfapps.eu12.hana.ondemand.com/transports"

CLIENT_ID = "sb-interview_demo_transport_app!b923597"
CLIENT_SECRET = "e5a58e12-6849-4833-8800-5eee585f347c$H0EkGqSXYJXVJTOMOocIcfufzbPmpeastGoMvrbKfIQ="
SCOPE = "interview_demo_transport_app!b923597.transportread"

payload = {
    "grant_type": "client_credentials",
    "response_type": "token",
    "scope": SCOPE
}
headers = {
    "Content-Type": "application/x-www-form-urlencoded"
}

token_resp = requests.post(AUTH_URL, data=payload, headers=headers, auth=(CLIENT_ID, CLIENT_SECRET))
token_json = token_resp.json()
print("Token response:", token_json)
