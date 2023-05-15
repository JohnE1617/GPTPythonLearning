#Write a Python function that takes a string representing a URL 
#as input and uses the urllib.parse module to extract the domain 
#name from the URL. Return the domain name as a string.

from urllib.parse import urlparse
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("u", type=str, nargs=1, default=None,help='url to be consumed')
args = parser.parse_args()
url = args.u[0]

def get_domain(url):
    domain = urlparse(url).netloc
    return domain

get_domain(url)
