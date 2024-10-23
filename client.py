import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 8080

client_socket.connect((host, port))

message = "Hello Server"
client_socket.send(message.encode('ascii'))

response = client_socket.recv(1024)
print(response.decode('ascii'))

client_socket.close()
