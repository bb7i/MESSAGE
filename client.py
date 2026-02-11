import socket
import threading

HOST = "192.168.56.1"
PORT = 65432

nickname = input()

def receive(sock):
    while True:
        data = sock.recv(1024)
        if not data or data == b"EXIT":
            sock.close()
            exit()
        print(data.decode())

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    threading.Thread(target=receive, args=(s,), daemon=True).start()

    while True:
        msg = input()
        if msg == "EXIT":
            s.sendall(b"EXIT")
            s.close()
            break
        s.sendall(f"{nickname}: {msg}".encode())
