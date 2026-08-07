# Week 5 · Day 1: OSI Model, Transport Protocols, & Logarithmic Searching

Today, I officially launched **Phase 2 (Core Cloud & Containers)**. I mastered the 7-layer OSI network standard, evaluated Layer 4 transport protocols, and engineered two globally optimized logarithmic search algorithms.

## What I Learned:
* **The OSI 7-Layer Model:** Mapped the physical path of network packets down from User Applications (Layer 7) through the Transport Layer (Layer 4), Network Layer (Layer 3), Data Link Layer (Layer 2), and onto the physical hardware cards (Layer 1).
* **Layer 4 Transport Protocols (TCP vs. UDP):**
  - **TCP (Transmission Control Protocol):** Connection-oriented (SYN -> SYN-ACK -> ACK). Guarantees reliability and flow-control. Used for secure web, SSH, and database streams.
  - **UDP (User Datagram Protocol):** Connectionless, ultra-fast "fire-and-forget" packets. Used when real-time speed overrides perfect data accuracy (multiplayer gaming like BGMI, VoIP, and DNS queries).
* **LeetCode #704 - Binary Search:** Implemented an $O(\log N)$ logarithmic search on sorted arrays using boundary-pointer squeezes. **Achieved 0 ms Runtime, beating 100.00% of Python submissions globally!**
* **LeetCode #35 - Search Insert Position:** Optimized boundary convergence logic to find sorted insert positions. **Achieved 0 ms Runtime, beating 100.00% of Python submissions globally!**
  - *Note: In accordance with DRY SRE principles, the Python files for these solutions are automatically committed and stored inside my dedicated [LeetCode-Logs](https://github.com/mohammedkaif911/LeetCode-Logs) repository.*

## Custom Projects & Labs Completed:
1. **OSI Network Architecture Drawing (Lab Page 15):** Hand-sketched the 7-layer stack inside my physical manual, mapping where HTTP, TCP, and IP each physically operate.