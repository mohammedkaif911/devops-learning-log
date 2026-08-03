# Week 3 · Day 6: Industrial Shell Automation & Sliding Window Optimization

Today, I engineered three production-grade Linux systems automation scripts, solved advanced dynamic sliding window algorithms, and completed the final master-level review of Week 3.

## What I Learned:
* **Industrial SRE Automation:** 
  - Written `disk_usage_report.sh` to parse root storage usage and trigger warnings based on custom safety thresholds.
  - Written `log_cleanup.sh` to recursively scan directories and purge outdated files (`-mtime +7`) using the native `find` utility.
  - Written `service_health_check.sh` utilizing process audits (`pgrep`) to automatically trigger systemd self-healing controls (`systemctl start`) if Nginx goes offline.
* **The Off-by-One Boundary Laws:** Mastered the mathematical inclusive/exclusive limits of range loops (`range(start, stop)`) and list slicings (`list[start:stop]`).
* **LeetCode #209 - Minimum Size Subarray Sum:** Designed an $O(N)$ dynamic sliding window that expands to the right and dynamically shrinks from the left while the sum is healthy ($\ge$ target) to find the absolute shortest contiguous subarray length.
* **LeetCode #121 - Best Time to Buy and Sell Stock (Sliding Window):** Re-coded the transaction tracker using a sliding window where the left boundary represents the best buy-day, sliding instantly on price drops.

## Scripts & Tools Completed:
1. `disk_usage_report.sh`: Audits root partition capacity and prints threshold warnings.
2. `log_cleanup.sh`: Safely purges log files older than 7 days from target directories.
3. `service_health_check.sh`: Automated Nginx daemon self-healing engine.
4. `LC_min_size_subarray.py`: Solves LeetCode #209 in-place in linear time.
5. `LC_best_time_stock_window.py`: Solves LeetCode #121 using dynamic window frames.