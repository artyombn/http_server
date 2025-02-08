import socket
import threading
import os

HOST = "localhost"
PORT = 8080
DOCUMENT_ROOT='./www'
def handle_request(client_socket):
    try:
        # 1. get request
        # 2. get hedares
        # 3. split headers to methoods
        # 4. give back response
        if method in ['GET', 'HEAD']:
            #create response ans send it back
            return
    finally:
        client_socket.close()

def start_server():
    #1. create socket
    #2. bind socket to address and port
    #3. in while loop create threads with fucntion for handle_request

if __name__ == "__main__":
    start_server()