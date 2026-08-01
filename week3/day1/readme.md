# Week 3 · Day 1: Bash Scripting Foundations & Dictionary Optimizations

Today, I mastered the variables and loop execution mechanics of native Bash scripting, analyzed Python Dictionary data structures, and optimized a key LeetCode search algorithm.

## What I Learned:
* **Bash Scripting Foundations:** Mastered the Shebang directive (`#!/bin/bash`). Learned strict variable assignment syntax (no spaces) and square bracket spacing requirements for conditionals.
* **String vs Integer Operators in Bash:** Identified that strings require algebraic signs (`==`, `!=`), while integers require text-based flags (`-eq`, `-gt`, etc.).
* **Dictionary Mechanics & Hashing:** Dictionaries use Hash Functions to map Keys directly to static physical addresses in RAM, bypassing the slow $O(N)$ linear scans of lists to achieve instant **$O(1)$ constant-time lookup**.
* **LeetCode #169 - Majority Element:** Coded an optimized $O(N)$ single-loop counter using a dictionary lookup, bypassing the slow $O(N^2)$ nested-count checks.
* **LeetCode #1 - Two Sum ($O(N)$ Revisited):** Rewrote the algorithm using the HashMap lookup table pattern. Used a single loop to calculate complements (`target - current`) and check historic states in $O(1)$ lookup time.

## Scripts & Automation Tools Completed:
1. `LC_MajorityElement.py`: Extracts the majority list element in O(N) linear time.
2. `LC_two_sum.py` (Revisited): The elite Two-Sum implementation using dynamic HashMap lookups.
3. `rename_bulk.sh`: A native Bash shell utility that scans a target folder and automatically renames all files matching a wildcard (`*.txt`) to include a clean date prefix.