import os
import requests
from dotenv import load_dotenv
from tabulate import tabulate

load_dotenv() # load the '.env' file

AUTH_URL = os.getenv("AUTH_URL")
TRANSPORT_URL = os.getenv("TRANSPORT_URL")

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
SCOPE = os.getenv("SCOPE")

# the function requests for OAuth token with the credentials available
# access token is returned on success, none on failure
def get_auth_token():
    payload = {
        "grant_type": "client_credentials",
        #"response_type": "token",
        "scope": SCOPE
    }
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    try:
        # POST request to token endpoint with HTTP Basic Auth using client ID & secret
        response = requests.post(AUTH_URL, data=payload, headers=headers, auth=(CLIENT_ID, CLIENT_SECRET))
        response.raise_for_status()  # raises error if HTTP status != 200
        # parsing JSON token from response
        token_json = response.json()
        token = token_json.get("access_token")
        if not token:
            print("token not found", token_json)
            return None
        return token
    except requests.RequestException as e:
        print(f"token access failed {e}")
        return None

# function to fetch the transport list using the received token
def fetch_transport_list(token):
    headers = {
        "Authorization": f"Bearer {token}"
    }
    try:
        # GET request to transport API
        response = requests.get(TRANSPORT_URL, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"list fetch failed: {e}")
        return None

# prints the transport list on success, none on failure
def print_transport_list(data):
    if not data:
        print("transport list print failed")
        return
# table rows of the transport list    
    table_rows = []
    for t in data:
        table_rows.append([
                t.get("id", ""), 
                t.get("description", ""),
                t.get("type", ""), 
                t.get("starttimestamp", ""), 
                t.get("endtimestamp", "")])
    headers = ["ID","Description", "Type", "starttimestamp", "endtimestamp"] # table header
    print(tabulate(table_rows, headers=headers))

# main flow for the program execution 
def main():
    token = get_auth_token()
    if not token:
        print("cannot continue without the authorization token")
        return
    transport_list = fetch_transport_list(token)
    # if API call fails, the ecexution stops
    if transport_list is None:
        print("transport list is empty or failed")
        return
    print_transport_list(transport_list) # print transport table to console

if __name__ == "__main__":
    main()    