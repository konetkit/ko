import subprocess

def ncat(host, port, listen=False):
    cmd = ["ncat"] if subprocess.call(["which", "ncat"], stdout=subprocess.DEVNULL) == 0 else ["nc"]
    if listen:
        cmd += ["-l", str(port)]
    else:
        cmd += [host, str(port)]

    subprocess.run(cmd)
