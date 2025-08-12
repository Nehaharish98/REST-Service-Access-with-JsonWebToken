import requests
from tabulate import tabulate

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
#print("Token:", token_json)

access_token = token_json.get("access_token")
if access_token:
    transport_headers = {"Authorization": f"Bearer {access_token}"}
    transport_resp = requests.get(TRANSPORT_URL, headers=transport_headers)
    data = transport_resp.json()
    print("Transport API status code:", transport_resp.status_code)
    print("Transport API raw JSON:", transport_resp.json())
else:
    print("No token and cannot fetch transport list")

#if isinstance(data, list) and data:
table_rows = []
for t in data:
    table_rows.append([
                t.get("id", ""), 
                t.get("description", ""),
                t.get("type", ""), 
                t.get("starttimestamp", ""), 
                t.get("endtimestamp", "")
            ])
        
headers = ["ID", "Type", "Start Time", "End Time", "Description"]
print(tabulate(table_rows, headers=headers, tablefmt="grid"))
#else:
        #print("No transport data available or bad format.")
