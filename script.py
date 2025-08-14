import os
import sys
import requests
from dotenv import load_dotenv
from tabulate import tabulate
from datetime import datetime

load_dotenv()  # load the '.env' file


def log_info(message):
    print(f"[INFO] {message}")


def log_error(message):
    print(f"[ERROR] {message}")


def log_warn(message):
    print(f"[WARN] {message}")


AUTH_URL = os.getenv("AUTH_URL")
TRANSPORT_URL = os.getenv("TRANSPORT_URL")

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
SCOPE = os.getenv("SCOPE")

# check for the .env file values
required_vars = ["AUTH_URL", "TRANSPORT_URL", "CLIENT_ID", "CLIENT_SECRET", "SCOPE"]

missing_vars = [var for var in required_vars if not os.getenv(var)]

if missing_vars:
    log_warn("set the values as per .env.example: {', '.join(missing_vars)}")
    sys.exit(1)


# the function requests for OAuth token with the credentials available
# access token is returned on success, none on failure
def get_auth_token():
    payload = {
        "grant_type": "client_credentials",
        # "response_type": "token",
        "scope": SCOPE,
    }
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    try:
        # POST request to token endpoint with HTTP Basic Auth using client ID & secret
        log_info("POST request OAuth access token...")
        response = requests.post(
            AUTH_URL, data=payload, headers=headers, auth=(CLIENT_ID, CLIENT_SECRET)
        )
        response.raise_for_status()  # raises error if HTTP status != 200
        # parsing JSON token from response
        token_json = response.json()
        token = token_json.get("access_token")
        if not token:
            log_error(f"token not found: {token_json}")
            sys.exit(1)
        log_info("access token success.")
        return token
    except requests.RequestException as e:
        log_error(f"token access failed: {e}")
        sys.exit(1)


# function to fetch the transport list using the received token
def fetch_transport_list(token):
    headers = {"Authorization": f"Bearer {token}"}
    try:
        # GET request to transport API
        log_info("GET request transport list from API...")
        response = requests.get(TRANSPORT_URL, headers=headers)
        response.raise_for_status()
        try:
            data = response.json()
        except ValueError:
            log_error("response was not valid JSON.")
            sys.exit(1)
        log_info(f"{len(data)} transport entries present in the list.")
        return data

    except requests.exceptions.RequestException as e:
        if response.status_code == 401:
            log_error("Unauthorized: token expired or invalid.")
        else:
            log_error(f"Failed to fetch transport list: {e}")
        sys.exit(1)


# prints the transport list on success, none on failure
def print_transport_list(data):
    if not data:
        print("transport list print failed")
        return
    # table rows of the transport list
    table_rows = []
    for t in data:
        table_rows.append(
            [
                t.get("id", ""),
                t.get("description", ""),
                t.get("type", ""),
                t.get("starttimestamp", ""),
                t.get("endtimestamp", ""),
            ]
        )
    headers = [
        "ID",
        "Description",
        "Type",
        "starttimestamp",
        "endtimestamp",
    ]  # table header
    print(tabulate(table_rows, headers=headers))
    log_info(
        f"{len(table_rows)} data is fetched at "
        f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}."
    )


# main flow for the program execution
def main():
    token = get_auth_token()
    transports = fetch_transport_list(token)
    print_transport_list(transports)


if __name__ == "__main__":
    main()
