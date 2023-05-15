#Implement a Python function that takes a list of URLs as input 
#and uses the requests library to send a GET request to each URL. 
#The function should return a dictionary where the keys are the 
#URLs, and the values are the corresponding response statuses 
#(e.g., 200, 404, etc.). Handle any exceptions that may occur 
#during the requests.

import requests
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("urls", help="Use this to eneter a list of urls, seperated by spaces", nargs='+',type=str)
parser.add_argument("d", help="input an existing dictionary", nargs='?',default={},type=dict)
args = parser.parse_args()
urls = args.urls
code_dict = args.d
error = None


def many_urls(urls, code_dict):
    for url in urls:
        try:
            response = requests.get(url)
            code_dict[url] = response.status_code
        except Exception as e:
            error = str(e)
    if error:
        print(error)
    return code_dict
    
many_urls(urls, code_dict)
