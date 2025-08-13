# ✅ Token Access and Service Access
- Checked if the Curl commands provided working
- Both token access and service access curl command worked and thr retreival of the transport list was successful on my local vs code terminal

# 🔍 Steps, understandings
- Reading the provided Curl commands for in detail understanding
- ## Token access curl command: OAuth 2.0 access token generation/retreival
    1. --request POST: HTTP POst request
    2. --url: where the access token is retreived
    3. --header: here the content type is mentioned, www-form-urlencoded is stated
    4. --data: grant_type=client_credentials-> means a OAuth 2.0 client credentials grant is used for client server communication(The client credentials grant type MUST only be used by confidential clients), response_type=token, client_id='', client_secret='',  scope=''
- ## Service access curl command:
    1. --request GET: getting the required data from the API
    2. --url: where the transport list is there
    3. --header: here the bearer token which is generated is pasted
    4. A bearer token is a security token used for authorization that allows anyone possessing it to access protected resources. It acts as a credential, granting access to the bearer without requiring further identification (The most common OAuth 2 token type)

# 💡 scripting steps or thoughts
- get the OAuth token using requests(get)
- check token validity ?
- get transport data from the api
- parse json and print
- tabulate output to console
- secure the sensitive data using .env.example and .env file
- validate responses before accessing data to avoid runtime errors
- find 401 Unauthorized status to check token expiration or invalidity
- add basic unit test for the script
- add linting with flake8 and formatting with black to maintain clean and consistent code style
- create a Makefile to automate install, test, lint, and format tasks
- pre-commit hooks for automating the run for linting and formatting checks before code commits

# 🧪 learnings,findings, etc,.
- .DS_Store gets created on running the script on local MacOS machine hidden system files created by Finder to store folder-specific display metadata such as icon positions, view mode, and window size. They appear automatically in every folder opened in Finder and help macOS retain folder appearance settings
- add this to the .gitignore
- adding the .env to .gitignore so that its not published or added to the main repo, which helps to keep the sensitive data private and secure
- additional .env.example is created to show someone like customer how to set up or enter the client id, secrect, scope
- edge case testing and handling: edge cases help identify unexpected behaviors and potential system vulnerabilities. Edge cases involve inputs or scenarios that push the limits of the API’s intended behavior, exposing bugs that may not be evident in normal conditions
- while running the tests today i encountered a error, where i had to start a unittest file name with test_XXX.py instead i had used tests_XXX.py
- i also learnt that in unit test the next improvements can be made adding the mock tests, which is helpful for speed and reliability as it focus tests on code’s logic, not the behavior or availability of external systems
- pre-commit run --all-files showed 4 lines 2 from script, 2 from test are exceeding the limit of black 88, made changes
