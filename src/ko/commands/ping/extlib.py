from pythonping import ping as ping_call

def ping(host, count=4):
    resp = ping_call(host, count=count)
    print(resp)
