import socket
import threading
import sys

def ncat(host, port, listen=False):
    if listen:
        server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_sock.bind((host, port))
        server_sock.listen(1)
        print(f"Listening on {host}:{port}...")
        conn, addr = server_sock.accept()
        print(f"Connection from {addr[0]}:{addr[1]}")
        sock = conn
    else:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((host, port))
        print(f"Connected to {host}:{port}")

    t1 = threading.Thread(target=handle_recv, args=(sock,), daemon=True)
    t1.start()
    try:
        if not listen:
            handle_send(sock)
    finally:
        sock.close()

def handle_recv(sock):
    try:
        while True:
            data = sock.recv(4096)
            if not data:
                break
            sys.stdout.write(data.decode(errors='ignore'))
            sys.stdout.flush()
    except Exception:
        pass

def handle_send(sock):
    try:
        while True:
            line = sys.stdin.readline()
            if not line:
                break
            sock.sendall(line.encode())
    except Exception:
        pass
