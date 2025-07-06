import telnetlib

def telnet(host, port):
    tn = telnetlib.Telnet(host, port, timeout=10)
    print(f"Trying {host}...\nConnected to {host}.\nEscape character is '^]'.")
    try:
        tn.interact()  # Chuyển stdin/stdout đến telnet session
    except KeyboardInterrupt:
        print("\nDisconnected.")
    tn.close()
