#Security best practices include hashing passwords instead of storing them in plain text. 
#Write a Python function that takes a password as input and returns its SHA-256 hash using 
#the hashlib module.

import requests
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('auth_token', type=str, help='Authorization token for API endpoint', nargs='?', default='guest_token')
args = parser.parse_args()

token = args.auth_token

def auth_request(url, token):
    headers = {
        'Authorization': token
    }
    response = requests.get(url,headers=headers)
    return response

url = "https://api.example.com/data"
response = auth_request(url, token)
try:
    if response.status_code == 200:
        print('Authorization Successful')
    else:
        print('Unauthorized, please check token')
except requests.exceptions.RequestException as e:
    print(f'Error has occured during the request: {e}')
