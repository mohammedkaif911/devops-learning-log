# Week 4 · Day 6: Virtual Environments & Advanced Recursion

Today, I mastered dependency isolation using Python virtual environments, and designed logarithmic recursive functions to manipulate string arrays and digit sums.

## What I Learned:
* **Dependency Isolation (venv):** Analyzed the threat of "Dependency Hell" in production. Configured isolated virtual environments (`python3 -m venv myenv`) and stepped inside using `source myenv/bin/activate`.
* **Dependency Manifests (`requirements.txt`):** Utilized `pip freeze > requirements.txt` to export precise project dependencies, enabling robust, zero-friction software replication.
* **Deep-Dive Recursion:** Mastered advanced recursive string-slicing and numerical modulo division. 
* **The Call Stack:** Evaluated how functions calling themselves allocate stack frames in RAM, and how to verify baseline stop checks to prevent stack-overflow crashes.

## Scripts & Tools Completed:
1. `verify_import.py`: A lightweight script validating requests connections inside our isolated virtual environment.
2. `requirements.txt`: Master dependency coordinate manifest.