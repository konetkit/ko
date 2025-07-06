import telnetlib
import sys

def telnet(host, port):
    tn = telnetlib.Telnet(host, port, timeout=10)
    print(f"Connected to {host}:{port}. Type Ctrl+C to exit.")
    try:
        tn.interact()  # Chuyển stdin/stdout đến telnet session
    except KeyboardInterrupt:
        print("\nDisconnected.")
    tn.close()
