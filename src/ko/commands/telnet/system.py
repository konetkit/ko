import subprocess

def telnet(host, port):
    subprocess.run(["telnet", host, str(port)])
