# Week 5 · Day 5: TLS/SSL Cryptography, Network Tunneling, & Stack/Queue Data Structures

Today, I advanced through Day 5 of SRE Core Networking and DSA. I traced the cryptographic handshake of HTTPS, mapped VPN gateways, and built my first stack and queue systems.

## What I Learned:
* **The TLS/SSL Handshake (HTTPS):**
  * **Asymmetric Encryption:** Leveraged to securely share a Pre-Master Secret using public and private key pairs.
  * **Symmetric Encryption:** Utilized modern AES-256 GCM to encrypt the actual web payload at lightning-fast speeds.
  * **Verbose handshakes:** Traced a live SSL connection using `curl -v`, identifying post-quantum hybrid ciphers (`X25519MLKEM768`), certificate checks, and ALPN HTTP/2 protocol agreements.
* **VPN Gateways & Network Tunneling:** Analyzed how a VPN Gateway server acts as an encrypted tunneling entry/exit point to bypass ISP (DNS-level) blocks.
* **LeetCode #232 - Implement Queue using Stacks:** Engineered a FIFO queue using two LIFO stacks. Managed element transfers to achieve an **Amortized $O(1)$ constant runtime** per operation.
* **LeetCode #155 - Min Stack:** Designed a custom stack that retrieves the minimum element in **$O(1)$ time** by implementing a secondary "twin" tracking stack in memory, trading memory space for CPU speed.

## SRE Labs Completed:
1. **Verbose Handshake Audit:** Executed a live network query on `example.com`, parsing DNS, TCP fallback, and cryptographic signatures directly inside the terminal.