# Week 3 · Day 5: Collaborative VCS Pipelines & Sliding Window Mechanics

Today, I mastered collaborative Pull Request (PR) pipelines on GitHub, successfully ran an advanced local Git branch recovery reset, and optimized complex sliding window algorithms.

## What I Learned:
* **The Pull Request (PR) Gate:** Mapped the production-grade Git review pipeline (Description specifications, testing checklists, and peer approval gates) to protect the stable `main` branch from buggy commits.
* **VCS Recovery Operations:** Resolved a local branch-commit conflict. Switched universes, pushed our target feature branch (`feat-pr-sandbox`), and forcefully reset our local `main` branch hard against `origin/main` to synchronize our local environment.
* **Sliding Window Mechanics:** 
  - Mastered using a fixed-size sliding frame (conveyor belt) to solve problems in $O(N)$ linear time by adding the entering element and subtracting the leaving element (`i - k`).
  - Mastered using a dynamic, rubber-band style "Expand and Shrink" window to evaluate non-repeating substrings, shrinking from the left inside a `while` loop whenever a duplicate element is encountered in our active set.

## Scripts Completed:
1. `LC_max_avg_subarray.py`: Solves LeetCode #643 using a fixed-size sliding window.
2. `LC_longest_substring.py`: Solves LeetCode #3 using a dynamic, set-based sliding window.