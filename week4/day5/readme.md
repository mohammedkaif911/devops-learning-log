# Week 4 · Day 5: File Streams & Recursion Foundations

Today, I mastered physical file descriptor management, designed error-safe directory stream parsers, and implemented low-level logarithmic recursion systems.

## What I Learned:
* **The File Descriptor (FD) Leak Hazard:** Mapped how unclosed OS file streams exhaust kernel resources, causing high-load servers to lock up and throw `Too many open files` errors.
* **The Context Shield (`with`):** Implemented Python's native Context Manager to automatically and forcefully release system file handles at the kernel level, even during runtime application crashes.
* **The Recursion Call-Stack:** Explored how recursive functions (calling themselves) allocate stacked execution frames in RAM ($O(N)$ Space), and why they require strict **Base Cases** (exits) to prevent Stack Overflow crashes.
* **LeetCode #231 - Power of Two:** Coded a secure recursive division algorithm using strict boundary base checks to reduce inputs logarithmically ($O(\log N)$ Time and Space).
* **LeetCode #70 - Climbing Stairs:** Optimized a classic DP sequence using a highly memory-efficient register-swapping loop, **achieving a 0 ms Runtime that beat 100.00% of all Python submissions globally!**

## Scripts & Projects Completed:
1. `sales_auditor.py`: A defensive SRE database utility that reads a local CSV flat file, parses fields using string splits, and prints formatted total revenues and top sales completely wrapped inside a `try/except FileNotFoundError` safety shield.
2. `sales.csv`: Active flat file representing our mock transactions inventory.