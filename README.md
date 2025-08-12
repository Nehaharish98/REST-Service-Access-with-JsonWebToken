# REST-Service-Access-with-JsonWebToken
A program that retrieves a list of transport from a secured service endpoint and prints the details to the console.

## How It Works
1. **Get OAuth Token** — POST to token endpoint with client credentials to get a bearer access token.  
2. **Fetch Transport List** — GET request to the transport list API with the token in the Authorization header.  
3. **Display Results** — Prints transport list in a neat table using `tabulate`.

## Setup & Run

### 1. Clone the Repo
```bash
https://github.com/Nehaharish98/REST-Service-Access-with-JsonWebToken.git
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure Environment
- The `.env` file stores sensitive data like CLIENT_ID and CLIENT_SECRET. It is **never committed** to Git
- The example env provided in `.env.example` file with placeholder keys to know what variables to set
- This step protects sensitive data out of the codebase, improving security and flexibility

### 4. Run the Script
```bash
python script.py
```

## Requirements
- Python 3.8+
- requests
- python-dotenv
- tabulate

## Developing, learning, findings Log
See my [`notes.md`] for more informations

# References
1. OAuth2.0 : https://oauthlib.readthedocs.io/en/latest/oauth2/grants/credentials.html
2. Bearer: https://oauthlib.readthedocs.io/en/latest/oauth2/tokens/bearer.html
3. .DS_Store: https://en.wikipedia.org/wiki/.DS_Store
4. python-dotenv: https://saurabh-kumar.com/python-dotenv/, https://www.geeksforgeeks.org/python/using-python-environment-variables-with-python-dotenv/
5. .env and .env.example: https://blog.quickadminpanel.com/how-to-use-laravel-env-example-files/
6. Handling empty or unexpected JSON data: https://realpython.com/python-json/#handling-json-empty-responses
7. Managing JSON parsing errors to prevent crashes: https://docs.python.org/3/library/json.html#json.JSONDecodeError
8. Dealing with OAuth token expiration and invalid tokens (HTTP 401): https://datatracker.ietf.org/doc/html/rfc6749#section-5.1 , https://auth0.com/blog/refresh-tokens-what-are-they-and-when-to-use-them/
9. curl command convertor: https://curlconverter.com/python/

I referenced official documentation and sources which i have referred to and tested incrementally.