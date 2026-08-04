# Week 4 · Day 1: Python Memory Physics & Defensive Scripting

Today, I mastered Python's pointer-based memory allocation engine, solved character-mapping stacks, and engineered a defensive, crash-proof interactive CLI.

## What I Learned:
* **Python Memory Physics:** Python variables are not static boxes; they are **Pointers** pointing to objects in RAM. Assigning variables `list_b = list_a` copies the pointer address, not the list, creating aliases. To clone objects, we must use copy constructors.
* **Conditional Short-Circuiting:** Python optimizes CPU cycles by skipping evaluation blocks inside compound `and`/`or` checks once the outcome is mathematically guaranteed.
* **The Stack (LIFO):** Mastered Last-In, First-Out data structures. Used `.append()` to push and `.pop()` to remove elements from the top of the stack.
* **LeetCode #344 - Reverse String:** Executed an in-place two-pointer boundary swap in $O(1)$ space.
* **LeetCode #20 - Valid Parentheses:** Scanned and validated nested brackets using a LIFO stack and HashMap. **Achieved 0 ms Runtime, beating 100.00% of Python submissions globally!**
* **Defensive Scripting:** Implemented a `try/except` shield to intercept `ValueError` casting exceptions, creating crash-proof, robust terminal tools.

## Scripts Completed:
1. `LC_reverse_string.py`: In-place string reversal using two-pointer swaps.
2. `LC_valid_parentheses.py`: 100% optimized bracket validation utilizing LIFO stacks.
3. `number_guesser_secure.py`: A crash-proof CLI game implementing active error-captures.