# Week 2 · Day 1: Linux Process Engineering & Advanced Algorithmic Sums

Today, I mastered how the operating system manages running programs (processes) and signals, and learned how to calculate the performance efficiency of my code using Big-O notation.

## What I Learned:
* **Process Anatomy:** Every running program is a Process. The OS tracks them using a unique **PID** (Process ID), a **PPID** (Parent Process ID), and a **UID** (User security ID).
* **Process Controls & Signals:** 
  - `ps aux` takes a global snapshot of all running processes.
  - `htop` displays live, real-time CPU and RAM telemetry.
  - `kill -15 [PID]` (SIGTERM) politely requests a process to exit safely.
  - `kill -9 [PID]` (SIGKILL) forces the kernel to instantly terminate a frozen process.
* **Systemd Daemons:** Learned about background services (daemons). Mastered `systemctl status/start/enable` to configure Nginx to boot up automatically on server start.
* **Big-O Notation:** A way to measure code efficiency:
  - **O(N) Time Complexity:** Execution time scales linearly with the list size (e.g. searching houses one-by-one).
  - **O(1) Space Complexity:** Memory footprint remains constant, regardless of input scale (e.g. using a single, static variables box).

## Scripts Completed:
1. `staircase.py`: Constructs a right-aligned staircase using string multipliers.
2. `mini_max_sum.py`: Calculates optimal min/max sums of 4 out of 5 integers in O(N) linear time.