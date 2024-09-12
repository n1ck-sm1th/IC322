#Telnet lecture.

import socket
import threading
import argparse
from random_username.generate import generate_username

# Parse command line arguments
parser = argparse.ArgumentParser(description="Simple Python Chat Server")
parser.add_argument('--port', type=int, default=12345, help='Port number to listen on (default: 12345)')
args = parser.parse_args()

host = '0.0.0.0'
port = args.port

# socket.socket() creates a Python object that describes the socket we want to create
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# socket.bind() makes a system call to the operating system saying "Please set up a mailbox for me for packets
# addressed to this host and port number."
server_socket.bind((host, port))
# socket.listen(5) makes another system call. This one tells the operating system "Start queuing incoming connections
# for me. If the queue reaches 5 connections that I haven't accepted yet, you can refuse more connections until I start
# accepting from the queue."
server_socket.listen(5)

# Later in the program we will use socket.accept(). This is the function that actually takes pending connections from the
# queue and sets up a working socket we can send/receive data through.

clients = []
usernames = {}

# Broadcast message to all clients
def broadcast(message, sender_socket=None):
    print(message.decode().strip())  # Print the message to the server's console
    for client in clients:
        if client != sender_socket:
            try:
                client.send(message)
            except:
                client.close()
                if client in clients:
                    clients.remove(client)

# Handle client connection
def handle_client(client_socket):
    # This try-except-finally block makes sure we cleanly disconnect all our clients (and
    # tear down the TCP connections) even if there is an error.
    try:
        username = generate_username()[0]
        usernames[client_socket] = username
        welcome_message = f"Your username is {username}. You can start chatting now.\n".encode()
        
        # socket.send() is how you send a message through a socket.
        client_socket.send(welcome_message)

        # broadcast() is a custom function I made. It uses the socket.send() function to
        # send a message to a list of sockets.
        broadcast(f"{username} has joined the chat!\n".encode(), client_socket)
        print(f"{username} connected")

        while True:
            # This is how you receive data from a socket. client_socket.recv() is
            # a blocking function.
            message = client_socket.recv(1024)
            if not message:
                break
            broadcast(f"{username}: {message.decode()}\n".encode(), client_socket)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        client_socket.close()
        if client_socket in clients:
            clients.remove(client_socket)
        if client_socket in usernames:
            broadcast(f"{usernames[client_socket]} has left the chat.\n".encode())
            del usernames[client_socket]



def accept_clients():
    print(f"Server started on port {port}")
    while True:
        # This is where we "bind to a port" and wait for clients to connect.
        # server_socket.accept() blocks until a connection is made.
        client_socket, addr = server_socket.accept()
        print(f"Connection from {addr}")
        clients.append(client_socket)
        # Since server_socket.accept() blocks its thread, in order to continue to service our
        # already-connected clients we need to create a new thread for every
        # connection.
        # The handle_client() function will be the function that actually sends and
        # receives messages from the client. This function only stands up the TCP connection
        # and "opens a socket". In order for handle_client() to send/receive messages, it
        # will need to know how to read/write to the socket we opened.
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

if __name__ == "__main__":
    accept_clients()
