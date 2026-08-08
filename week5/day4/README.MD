# Week 5 · Day 4: Load Balancer Architectures & Rotated Logarithmic Search

Today, I advanced through Day 4 of SRE Networking and DSA. I evaluated OSI traffic-routing layers on load-balanced pools and engineered an optimized searching algorithm to handle shifted arrays.

## What I Learned:
* **Load Balancer Architectures (L4 vs. L7):**
  * **Layer 4 Load Balancing:** Routes traffic strictly at the Transport Layer (Layer 4) using source/destination IPs and ports. Ultra-fast, low overhead, but blind to application payloads.
  * **Layer 7 Load Balancing:** Decrypts SSL/TLS certificates and opens HTTP/HTTPS payloads at the Application Layer (Layer 7). Enables smart path-based routing (e.g., `/api` to different backends) and utilizes session cookies (Sticky Sessions/Session Affinity) to preserve user states across distributed clusters.
* **LeetCode #33 - Search in Rotated Sorted Array:** Engineered an $O(\log N)$ search algorithm on shifted arrays. Leveraged the mathematical insight that cutting a rotated array in half always yields at least one strictly sorted sub-array, allowing precise boundary squeezes using nested conditional scopes. **Achieved 0 ms Runtime, beating 100.00% of Python submissions globally!**

## SRE Labs Completed:
1. **Load Balancing Incident Diagnosis:** Modeled and resolved a production-grade session state loss (empty shopping carts) by simulating the operational benefits of migrating from connection-blind Layer 4 backends to cookie-aware Layer 7 backends.