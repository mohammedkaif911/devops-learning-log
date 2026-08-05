import socket
target = "127.0.0.1"
ports_to_scan = [21, 22, 80, 443, 2220, 8080]
print("=========================================")
print("★ SRE ACTIVE NETWORK PORT SCANNER ★")
print("=========================================")
print("Scanning target: 127.0.0.1")
for port in ports_to_scan:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.3)
    result = s.connect_ex((target, port))
    if result == 0:
        print(f"[OPEN] Port {port} is active! Active service detected.")
    else:
        print(f"[CLOSED] Port {port} is secured.")
    s.close()