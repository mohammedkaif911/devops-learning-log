# Week 2 · Day 3: Package Managers & LeetCode Foundations
## THE PREFIX OF LC_ IN PYTHON FILES IS REFERED TO THE LEET CODE PROBLEMS :)
Today, I mastered how the operating system handles software lifecycles via package repositories, and successfully solved my first two primary LeetCode algorithmic challenges.

## What I Learned:
* **Package Managers & Repos:** Repositories are secure cloud vaults run by OS distributions. Linux uses package managers to download, install, and resolve software dependencies instantly.
* **APT CLI Toolkit:**
  - `apt update` refreshes local package indexes (does not install/upgrade).
  - `apt install [package] -y` downloads and installs binaries.
  - `apt remove` deletes binaries but leaves configurations.
  - `apt purge` deletes everything (binaries + configurations), keeping disk space optimal.
* **LeetCode #1 - Two Sum:** Implemented a nested loop ($O(N^2)$ time) and optimized it utilizing immediately triggered `return` exits. 
* **LeetCode #121 - Best Time to Buy and Sell Stock:** Implemented an $O(N)$ linear time and $O(1)$ space algorithm tracking trailing minimums and record profits. Mastered using `float('inf')` as a safety placeholder.

## Scripts Completed:
1. `LC_two_sum.py`: Solves LeetCode #1 using nested loops and immediate function exits.
2. `LC_best_time_stock.py`: Solves LeetCode #121 using single-pass tracking and boundary comparisons.(was quite confusing but nothings impossible)