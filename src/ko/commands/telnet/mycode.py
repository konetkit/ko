import socket
import threading
import sys

def telnet(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))
    print(f"Connected to {host}:{port}. Type Ctrl+C to exit.")

    t = threading.Thread(target=recv_thread, args=(sock,), daemon=True)
    t.start()

    try:
        while True:
            line = sys.stdin.readline()
            if not line:
                break
            sock.sendall(line.encode())
    except KeyboardInterrupt:
        print("\nDisconnected.")
    finally:
        sock.close()

def recv_thread(sock):
    while True:
        try:
            data = sock.recv(1024)
            if not data:
                break
            print(data.decode(errors='ignore'), end='')
        except:
            break
