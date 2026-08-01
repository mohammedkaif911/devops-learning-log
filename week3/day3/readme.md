# Week 3 · Day 3: Version Control Internals & Two-Pointer Squeezing

Today, I mastered the internal physical state-transitions of Git, solved an optimal boundary-squeezing search, and wrote a 100%-beats-world array-deduplication algorithm.

## What I Learned:
* **Git Version Control Architecture:** Git is a 3D time-travel database. Local files travel through three distinct physical states in memory:
  - Working Directory (Modified/Red text) -> staged via `git add` to the:
  - Staging Area (Prepared/Green text) -> sealed via `git commit` to the:
  - Local Repository (Saved inside the hidden `.git/` database).
* **Git Disaster Recovery:** Mastered how `git checkout [hash]` rolls back the entire local disk's files to any historical snapshot in 1 second.
* **LeetCode #167 - Two Sum II (Sorted):** Leveraged sorted arrays to solve Two Sum in an optimal $O(1)$ constant space using a Two-Pointer "boundary squeeze" (sliding `left` and `right` inward), eliminating dictionary memory overhead.
* **LeetCode #26 - Remove Duplicates from Sorted Array:** Developed a Two-Pointer "write-forward" scan to filter duplicates in-place, bypassing expensive memory shifting. **Achieved the absolute hardware speed limit: 0 ms Runtime, beating 100.00% of all Python submissions globally!**

## Scripts Completed:
1. `LC_two_sum_sorted.py`: Squeezes sorted arrays in-place using boundary pointers.
2. `LC_remove_duplicates.py`: Dedups sorted arrays in-place using write-forward pointers (100% globally optimized).