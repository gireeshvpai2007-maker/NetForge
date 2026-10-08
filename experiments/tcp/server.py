import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(("127.0.0.1", 5000))
server.listen()

print("Server waiting for connection...")

connection, address = server.accept()

print("Connected:", address)

message = connection.recv(1024).decode()
print("Client:", message)

connection.send("Hello from server!".encode())

connection.close()
server.close()