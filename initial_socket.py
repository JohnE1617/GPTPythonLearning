#Network sockets allow communication between different machines over a network. 
#Write a Python function that creates a TCP socket, connects to the host "www.example.com" 
#on port 80, sends the string "GET / HTTP/1.1\r\nHost: www.example.com\r\n\r\n", and
#prints the response received from the server.

#!/usr/env python3

import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ("www.example.com", 80)

request = "GET / HTTP/1.1\r\nHOST: www.example.com\r\n\r\n"

client_socket.connect(server_address)

try:
    client_socket.sendall(request.encode())

    response = client_socket.recv(4096)
    print(response.decode())
except Exception as e:
    print(f"there was an error {e}")
finally:
    client_socket.close()
