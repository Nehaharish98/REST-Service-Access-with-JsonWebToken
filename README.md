# REST-Service-Access-with-JsonWebToken
A program that retrieves a list of transport from a secured service endpoint and prints the details to the console.


# Environment Setup
- The `.env` file stores sensitive data like CLIENT_ID and CLIENT_SECRET. It is **never committed** to Git.
- The example env provided in `.env.example` file with placeholder keys to know what variables to set.
- This step protects sensitive data out of the codebase, improving security and flexibility.

# References
1. OAuth2.0 : https://oauthlib.readthedocs.io/en/latest/oauth2/grants/credentials.html
2. Bearer: https://oauthlib.readthedocs.io/en/latest/oauth2/tokens/bearer.html
3. .DS_Store: https://en.wikipedia.org/wiki/.DS_Store
4. python-dotenv: https://saurabh-kumar.com/python-dotenv/, https://www.geeksforgeeks.org/python/using-python-environment-variables-with-python-dotenv/
5. .env and .env.example: https://blog.quickadminpanel.com/how-to-use-laravel-env-example-files/