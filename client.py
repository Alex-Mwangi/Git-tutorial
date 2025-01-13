import socket

def start_client():
    host = '127.0.0.1'  # The same as the server's hostname
    port = 5000          # The same port number used by the server

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    print("Connected to the server. Type 'bye' to exit the chat.")
    while True:
        message = input("Client: ")
        client_socket.send(message.encode())
        if message.lower() == 'bye':
            print("Chat ended by client.")
            break
        
        data = client_socket.recv(1024).decode()
        if not data or data.lower() == 'bye':
            print("Chat ended by server.")
            break
        print(f"Server: {data}")
    
    client_socket.close()

if __name__ == "__main__":
    start_client()
