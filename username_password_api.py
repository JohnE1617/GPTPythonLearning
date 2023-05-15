#Write a Python function that uses the requests library to make a 
#POST request to the URL "https://api.example.com/login" with a JSON 
#payload containing a username and password. The function should return 
#the response from the server.

#!/usr/env python3
parser = argparse.ArgumentParser()
parser.add_argument('auth_token', type=str, help='Authorization token for API endpoint')
args = parser.parse_args()

token = args.auth_token

def auth_request(url, token):
    headers = {
        'Authorization': token
    }
    response = requests.get(url,headers=headers)
    return response

url = "https://api.example.com/data"
auth_request(url, token)
