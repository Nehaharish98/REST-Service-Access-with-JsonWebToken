import unittest
import script

class TestTransportAPI(unittest.TestCase): # test case class is defined
    # basic tests which calls the real get_auth_token and should have correct values in .env to pass the test
    def test_get_auth_token(self):
        token = script.get_auth_token() 
        self.assertIsNotNone(token, 'Token Authentication failed')

    #real token is used here to get the transport list, checks if the API fetching function works or not
    def test_fetch_transport_list(self):
        token = script.get_auth_token() # fetching a token
        data = script.fetch_transport_list(token) 
        self.assertIsInstance(data, list, "Transport data is list")

if __name__ == "__main__":
    unittest.main()