from email import message
import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 555

client_socket.connect((host, port))

message = client_socket.recv(1024)

client_socket.close()

print(message.decode("ascii"))