# SRE Active Network Port Scanner (Nmap Simulation)

A lightweight, high-performance network security scanner written in Python. It interacts directly with the system's network interface card to audit open TCP ports on local or remote servers.

## Features & SRE Concepts:
* **Asymmetric Network Socket Probing:** Utilizes Python's built-in `socket` library to initialize raw IPv4 TCP socket channels (`socket.AF_INET`, `socket.SOCK_STREAM`) in memory.
* **Non-Blocking Timeout Controls:** Implements strict connection timeouts (`s.settimeout(0.3)`) to prevent terminal hangs on closed ports, ensuring lightning-fast execution speeds.
* **Low-Level Handshake Verification:** Leverages the native `connect_ex` socket method to execute low-level TCP connection handshakes. Returns a clean execution result code (`0` for success/open, and error codes for closed).
* **VCS Portability:** Built as an independent sandbox utility complete with developer documentation.

## How to Run:
Navigate to this directory and run the scanner:
```bash
python3 port_scanner.py