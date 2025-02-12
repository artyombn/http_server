import socket
import threading
import os

HOST = "localhost"
PORT = 8080
DOCUMENT_ROOT="./www"
HDRS = 'HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n'
HDRS_404 = 'HTTP/1.1 404 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n'


def handle_request(client_socket):
    try:
        data = client_socket.recv(1024).decode("utf-8")
        # 1. get request
        request = data.split("\n")[0]
        # 2. get headers
        headers = data.split("\n")[1:]
        # 3. split headers to methods
        method, url, version = request.split(" ")
        # 4. give back response
        if method in ['GET', 'HEAD']:
            content = load_page_from_get_request(url)
            client_socket.send(content)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        client_socket.close()


def load_page_from_get_request(url):
    response = ''
    try:
        if url == '/':
            url = '/index.html'

        file_path = os.path.join('views', url.lstrip('/'))
        with open(file_path, "rb") as file:
            response = file.read()
        return HDRS.encode('utf-8') + response
    except FileNotFoundError:
        return (HDRS_404 + 'Sorry, bro! No page found...').encode('utf-8')

def start_server():
    try:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((HOST, PORT))
        server.listen(1000)

        while True:
            print(f"Server is working...")
            client_socket, address = server.accept()
            client_handler = threading.Thread(target=handle_request, args=(client_socket,))
            client_handler.start()
    except KeyboardInterrupt:
        server.close()
        print(f"Shutdown server...")


if __name__ == "__main__":
    start_server()