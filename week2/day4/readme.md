# Week 2 · Day 4: SSH Key Handshakes, Array Reductions & SRE Automation

Today, I mastered how secure public-key cryptography authenticates remote system logins, solved a complex contiguous subarray optimization algorithm, and built a custom Linux system resource monitor.

## What I Learned:
* **SSH Key Architecture:** SSH keys use asymmetric cryptography (private key is the secret key; public key is the public lock). Stolen keys allow absolute shell access - protect them with strict file permissions (`600`/`700`) and passphrases.
* **Server Verification (`known_hosts`):** Client caches server host fingerprints inside `~/.ssh/known_hosts` on the first connection to prevent Man-in-the-Middle spoofing.
* **LeetCode #217 - Contains Duplicate:** Checked duplicates in $O(N)$ linear time by comparing array lengths against unique HashSet reductions.
* **LeetCode #53 - Maximum Subarray (Kadane's):** Solved an $O(N)$ contiguous sum array challenge. Identified and resolved a critical logic branching bug where `elif` statements bypassed accumulator resets when new negative maximum records were updated.
* **Kernel Probing:** Discovered how the Linux kernel exposes live system telemetry inside virtual memory files (`/proc/meminfo` and `/proc/loadavg`), and how Python reads these directly to audit RAM and CPU loads.

## Custom Projects & Scripts Completed:
1. `LC_contains_duplicate.py`: Identifies array duplication using HashSet comparisons.
2. `LC_max_subarray.py`: Solves LeetCode #53 using Kadane's Algorithm with independent execution checks.
3. `sys_monitor.py`: A custom, lightweight SRE diagnostic tool that queries Linux `/proc` systems to audit hard drive space, RAM usage percentages, and active CPU averages.

---

## 🛠️ How to Run Your System Monitor:
To execute a live diagnostic audit of your machine's resources, run this command in your terminal:
```bash
python3 sys_monitor.py