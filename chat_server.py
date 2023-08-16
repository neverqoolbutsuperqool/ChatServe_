import socket
import threading

# Server configuration
HOST = '127.0.0.1'
PORT = 12345
ADDRESS = (HOST, PORT)

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the address
server_socket.bind(ADDRESS)

# Listen for incoming connections
server_socket.listen()

print(f"Server is listening on {HOST}:{PORT}")

# List to store client connections
clients = []

# Function to handle individual client connections
def handle_client(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            print(message)
            # Broadcast the message to all clients
            for client in clients:
                if client != client_socket:
                    try:
                        client.send(message.encode('utf-8'))
                    except:
                        clients.remove(client)
        except:
            clients.remove(client_socket)
            break

# Accept and handle incoming connections
while True:
    client_socket, client_address = server_socket.accept()
    clients.append(client_socket)
    print(f"Connected with {client_address}")
    client_thread = threading.Thread(target=handle_client, args=(client_socket,))
    client_thread.start()
