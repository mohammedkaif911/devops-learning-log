# Week 3 · Day 2: Bash Functions & Advanced Array Reductions

Today, I mastered parameter scoping and command-line argument handling in Bash, solved a binary bitwise reduction algorithm, and engineered an optimized string sanitization logic.

## What I Learned:
* **Bash Functions & Arguments:** Functions do not define parameter arrays inside parentheses. Instead, Bash utilizes global **Position Parameters** (`$1`, `$2`, `$@`) to accept command-line arguments.
* **Script vs. Function Scoping:** Mapped how `$#` (Argument Count) behaves differently inside functions vs. global script scopes. Emplaced script-level parameter validations at the top of configuration scripts using the `exit 1` safety shutdown directive.
* **LeetCode #136 - Single Number:** Implemented an ultra-optimal $O(N)$ time and $O(1)$ space bitwise **XOR (`^`)** reduction. Leveraged hardware-level bitwise self-cancellation to isolate a unique integer without allocating auxiliary memory tables.
* **LeetCode #125 - Valid Palindrome:** Sanitized raw string data using alphanumeric scans (`.isalnum()`) and case-normalizations. Optimized memory structures by comparing sanitized lists directly using list-slicing (`[::-1]`), bypassing redundant string generation overhead.

## Scripts & Projects Completed:
1. `LC_single_number.py`: Isolates unique integers using register-level XOR operations.
2. `LC_is_palindrome.py`: Audits alphanumeric palindromes using optimized list comparisons.
3. `backup.sh`: A production-grade backup script that audits source directories (`! -d`) and utilizes command-substitution to generate non-overwriting, timestamped archives.