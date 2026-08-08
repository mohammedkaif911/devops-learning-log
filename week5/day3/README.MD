# Week 5 · Day 3: DNS Record Architectures, Manual Merge Sort, & Rotated Binary Squeezing

Today, I advanced to Day 3 of SRE Core Networking and DSA. I mastered Authoritative DNS record configurations, wrote my first recursive divide-and-conquer sorting algorithm, and solved search state rotations.

## What I Learned:
* **DNS Record Architectures:**
  * **A Record:** Maps a domain name directly to an IPv4 address.
  * **CNAME Record:** Maps an alias domain to another domain, trading a double lookup latency penalty for absolute routing elasticity.
  * **MX Record:** Directs mail routing to company servers (such as Google Workspace) using relative priorities.
  * **TXT Record:** Hosts arbitrary validation data and secure mail whitelists (SPF/DKIM/DMARC) to block domain-spoofing spammers.
* **Merge Sort ($O(N \log N)$):** Engineered my first recursive, divide-and-conquer sorting algorithm. Understood how Python manages the call stack limit via memory safety features and how pointer indexing (`i`, `j`, `k`) handles the merging and cleanup states.
* **LeetCode #153 - Find Minimum in Rotated Sorted Array:** Optimized standard binary search to track drop boundaries (inflection points) on shifted arrays in $O(\log N)$ logarithmic time, squeezing boundaries using a single conditional check against the rightmost pointer.

## SRE Labs Completed:
1. **My First Merge Sort Implementation:** Built and ran a complete, recursive sorting script, tracing how arrays divide to size 1 and merge back in physical memory.