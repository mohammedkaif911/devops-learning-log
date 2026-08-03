import sys

if (len(sys.argv) -1) < 1:
    print("Error: Missing port parameter. Usage: python3 port_auditor.py [port_number]")
    sys.exit(1)

port = sys.argv[1]
port_int = int(port)

if port_int == 22 or port_int == 2220:
    print(f"[PASS] Port {port_int} is a secure shell channel.")
elif port_int == 80 or port_int == 8080:
    print(f"[WARNING] Port {port_int} uses unencrypted HTTP traffic. Security risk!")
else:
    print(f"[INFO] Port {port_int} status: Normal.")