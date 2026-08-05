# Week 3 · Day 3: SRE Python Refactoring & Complexity Audits

Today, I mastered Big-O mathematical complexities, audited the performance scaling of my active codebase, and executed a complete system migration refactoring Bash scripts into reusable Python functions.

## What I Learned:
* **The Big-O Performance Spectrum:**
  - $O(1)$ Constant Time: Lookup times remain static regardless of system scale. (e.g. Dictionary Hash Map searches).
  - $O(N)$ Linear Time: Execution scales proportionally with data increments. (e.g. Single-loop scans).
  - $O(N^2)$ Quadratic Time: Execution scales exponentially. Triggered primarily by nested loop structures. (e.g. Brute-force Two-Sum).
* **System Refactoring & Migration:** Migrated procedural Bash shell scripts into modular, exception-safe Python functions. Used the **`*args`** unpacking tuple parameter to design a dynamic bulk renamer that accepts arbitrary file arrays.

## Scripts & Tools Completed:
1. `refactor_tools.py`: A dual SRE utility containing:
   - `bulk_rename(date_prefix, *files)`: Custom renamer accepting a variable file array (`*args`).
   - `backup_directory(source_dir, backup_parent)`: Secure backup utility with automated timestamping and active folder validations.