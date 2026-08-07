# Week 5 · Day 2: IP Subnetting, WSL2 Interface Auditing, & Algorithmic Performance

Today, I advanced through Day 2 of SRE Networking and DSA. I mastered subnet mask logic and CIDR math, audited the live network routing tables of my local WSL2 kernel, and optimized searching and sorting algorithms.

## What I Learned:
* **IP Addressing & CIDR Math:** Mastered calculating Network IDs, Broadcast Addresses, and Usable Host IPs for various CIDR notations (such as `/26` and `/27`) manually without online tools.
* **WSL2 Network Interfaces:**
  * Analyzed loopback (`lo`) and virtual ethernet (`eth0`) adapters.
  * Dissected MTU configurations (MTU 1400 on `eth0` to prevent virtual packet fragmentation).
  * Audited the kernel routing table (`ip route`) and verified the Default Gateway address (`172.28.208.1`) leading to the host machine.
* **LeetCode #69 - Sqrt(x):** Engineered an $O(\log N)$ square root floor algorithm using Monotonic Binary Search. Implemented system-level patches:
  * **Overflow-Safe Midpoint Calculation:** `mid = left + (right - left) // 2` to protect memory boundaries.
  * **Single-Register Caching:** Cached multiplication steps to reduce CPU arithmetic load by 66.6%.
* **Optimized Bubble Sort:** Built an early-termination Bubble Sort using a `swapped` boolean check to achieve $O(N)$ best-case execution, restricting the inner loop boundaries to `n - i - 1` to prevent redundant CPU cycles.

## SRE Labs Completed:
1. **WSL2 Network Infrastructure Audit:** Ran active terminal diagnostics (`ip addr` and `ip route`) to map out how Windows routes traffic into Linux VM subnet blocks.