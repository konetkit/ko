import socket
import os
import struct
import time

def checksum(data):
    if len(data) % 2:
        data += b'\x00'
    s = sum((data[i] << 8) + data[i+1] for i in range(0, len(data), 2))
    s = (s >> 16) + (s & 0xffff)
    s += s >> 16
    return ~s & 0xffff

def ping(host, count=4, timeout=1.0):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
        sock.settimeout(timeout)
    except PermissionError:
        print("Permission denied: need to run as root/admin to use RAW sockets.")
        return

    pid = os.getpid() & 0xFFFF

    for seq in range(count):
        # Build packet
        header = struct.pack("!BBHHH", 8, 0, 0, pid, seq)
        payload = b'ko_ping' * 8
        chksum = checksum(header + payload)
        header = struct.pack("!BBHHH", 8, 0, chksum, pid, seq)
        packet = header + payload

        try:
            sock.sendto(packet, (host, 0))
            start = time.time()
            while True:
                data, addr = sock.recvfrom(1024)
                icmp_header = data[20:28]
                r_type, code, _, r_id, r_seq = struct.unpack("!BBHHH", icmp_header)
                if r_id == pid and r_seq == seq:
                    rtt = (time.time() - start) * 1000
                    print(f"Reply from {addr[0]}: seq={seq} time={rtt:.2f} ms")
                    break
        except socket.timeout:
            print(f"Request timed out for seq={seq}")
        except Exception as e:
            print(f"Error: {e}")
        time.sleep(1)

    sock.close()
