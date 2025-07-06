import subprocess

def ping(host, count=4):
    cmd = ["ping", "-c", f"{count}", host]
    subprocess.run(cmd)
