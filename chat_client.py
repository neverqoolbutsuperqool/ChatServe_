import socket
import threading

# Client configuration
HOST = '127.0.0.1'
PORT = 12345
ADDRESS = (HOST, PORT)

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect(ADDRESS)

# Function to receive messages from the server
def receive_messages():
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            print(message)
        except:
            print("Connection to server lost.")
            break

# Start a thread to receive messages
receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

# Main loop to send messages
try:
    while True:
        message = input()
        if message.lower() == 'exit':
            break
        client_socket.send(message.encode('utf-8'))
except KeyboardInterrupt:
    pass

# Close the client socket
client_socket.close()
