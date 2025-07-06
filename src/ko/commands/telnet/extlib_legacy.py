import sys
import telnetlib

def telnet(host, port):
    if sys.version_info >= (3, 13):
        print("The telnetlib was removed in Python 3.13 after being deprecated in Python 3.11. " +
            "The removal was decided in PEP 594.")
        return
    tn = telnetlib.Telnet(host, port, timeout=10)
    print(f"Trying {host}...\nConnected to {host}.\nEscape character is '^]'.")
    try:
        tn.interact()  # Chuyển stdin/stdout đến telnet session
    except KeyboardInterrupt:
        print("\nDisconnected.")
    tn.close()
