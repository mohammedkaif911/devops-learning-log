# Week 2 · Day 5: OS Shell Customization & Advanced Array Algorithms

Today, I mastered environment variable routing, configured persistent terminal customizations via hidden startup configurations, and analyzed modular algorithm branching logic.

## What I Learned:
* **Environment Variables & $PATH:** Explored how the OS uses variables (like `$USER` and `$HOME`) globally. Mapped how the `$PATH` variable sequentially searches directory chains to execute binary commands.
* **Shell Customization (.bashrc):** Configured persistent, colored terminal banners and custom SRE macros (Aliases) inside the hidden startup script `~/.bashrc`.
* **LeetCode #283 - Move Zeroes:** Implemented an in-place Two-Pointer swap algorithm running in $O(N)$ time and $O(1)$ space. Mastered Python's parallel tuple assignment to execute variable swaps without temporary memory allocations.
* **LeetCode #88 - Merge Sorted Array:** Analyzed reverse three-pointer logic to merge sorted arrays in-place from back-to-front, mitigating array-shifting bottlenecks.

## Scripts Completed:
1. `LC_move_zeroes.py` (Added to day5): Pushes array zeroes to the end in-place using two-pointer swaps.
2. `LC_merge_sorted_array.py` (Added to day5): Merges sorted arrays back-to-front using three-pointer offsets.