import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 555

server_socket.bind((host, port))

server_socket.listen(5)

while True:
    client_socket, address = server_socket.accept()
    print("connection from " +  str(address))

    message = "you are connected to the server" + "\r\n"
    client_socket.send(message.encode("ascii"))

    client_socket.close()