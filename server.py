import socket

HOST = "192.168.56.1"
PORT = 65432

clients = []

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()

    while len(clients) < 2:
        conn, _ = s.accept()
        clients.append(conn)

    while True:
        for i in range(2):
            data = clients[i].recv(1024)
            if not data:
                for c in clients:
                    c.close()
                exit()

            if data == b"EXIT":
                clients[1 - i].sendall(b"EXIT")
                for c in clients:
                    c.close()
                exit()

            clients[1 - i].sendall(data)
