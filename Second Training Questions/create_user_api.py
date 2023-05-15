#Write a Python function that uses the requests library to send a POST 
#request to the URL "https://api.example.com/create-user" with a JSON 
#payload containing a username and password. Handle any exceptions that 
#may occur during the request and return the response from the server.

#/usr/env python3

import requests
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("username", type=str, help="User name to check", nargs='?',default='guest')
parser.add_argument("password", type=str, help="password for user created",nargs='?',default='password1')

def create_user(user, password):
  payload = {
    "username":f"{user}",
    "password":f"{password}"
  }
  url = 'https://api.example.com/create-user'
  try:
    response = requests.post(url, json=payload)
  except Exception as e:
    response = str(e)
  return response

create_user(username, password)

