#Implement a Python function that accepts an IP address as input 
#and checks if it is valid. The function should return a boolean 
#value indicating whether the IP address is valid or not.

import argparse
import re

parser = argparse.ArgumentParser()
parser.add_argument('ip', help='IP to check for validity', nargs='?', default ='0.0.0.0', type=str)
args = parser.parse_args()
IP = args.ip
result = None

def valid_ip(ip):
    pattern = r'^(\d{1,3}\.){3}\d{1,3}$'
    result = re.match(pattern, ip)
    if result:
        ip_split = ip.split('.')
        ip_split = [int(num) for num in ip_split]
        if len(ip_split) != 4:
            return print(f"{ip} is not a valid IP address")
        else:
            for number in ip_split:
                if 0 > number or number > 255:
                    return print(f"{ip} is not a valid IP address")
                else:
                    return print(f"{ip} is a valid IP address")
    else:
        return print(f"{ip} is not a valid IP address")

try:
    valid_ip(IP)
except Exception as e:
    print(f'There was an error running the program: {e}')
