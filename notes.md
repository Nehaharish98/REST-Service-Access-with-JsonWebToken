# Token Access and Service Access
- Checked if the Curl commands provided working 
- Both token access and service access curl command worked and thr retreival of the transport list was successful on my local vs code terminal

# Steps 
- Reading the provided Curl commands for in detail understanding 
- Token access curl command:
    - --request POST: HTTP POst request
    - --url: where the access token is retreived 
    - --header: here the content type is mentioned, www-form-urlencoded is stated
    - --data: grant_type=client_credentials-> means a OAuth 2.0 client credentials grant is used for client server communication(The client credentials grant type MUST only be used by confidential clients), response_type=token, client_id='', client_secret='',  scope=''
    - A bearer token is a security token used for authorization that allows anyone possessing it to access protected resources. It acts as a credential, granting access to the bearer without requiring further identification.
- Service access curl command:    
    - --request GET:
    - --url:
    - --header: