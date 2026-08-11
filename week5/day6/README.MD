# Week 5 · Day 6: Network Diagnostics Arsenal & The Monotonic Stack Finale

Today, I closed out Week 5 with a full diagnostic lab day — weaponizing the SRE network-troubleshooting toolkit across live incident scenarios — and unlocked the most powerful stack pattern of the module to finish the Stacks & Queues arc.

## What I Learned:
* **The Monotonic Stack Pattern (NEW WEAPON):**
  * **The Invariant:** A stack that enforces order on its own contents — indices of days piled up in strictly decreasing temperature, each waiting for a hotter day to settle its account.
  * **Why Indices, Not Values:** The answer is a *distance* (`i - prev`), which requires positions. A single stored index yields both the position directly and the temperature via one lookup — one index, two powers.
  * **The O(N) Accounting Argument:** Each index is pushed exactly once and popped at most once, so total work across the nested loops is ≤ 2N operations. The inner `while` never re-scans — it only resolves days already waiting.
  * **Design, Not Magic:** Pre-filling `answer = [0] * n` handles the "no warmer day exists" case for free — days never popped simply keep their default 0.
* **LeetCode #739 - Daily Temperatures (Medium):** Engineered an O(N) monotonic stack solution to compute days-until-warmer for every element. **Achieved 84 ms runtime, beating 85.07% of Python submissions, at 28.3 MB memory (beating 67.7%)!**
* **LeetCode #682 - Baseball Game:** Stack-based scorekeeping with undo/invalidation semantics (`C`, `D`, `+` operations). **Achieved 0 ms runtime, beating 100.00% of Python submissions globally!**

## SRE Labs Completed:
1. **5-Scenario Connection Diagnosis:** Deployed the full diagnostics arsenal — `ping` (reachability & ICMP latency), `traceroute` (hop-by-hop path mapping), `dig` (DNS record interrogation), `netstat` (socket & port-state auditing), and `curl -v` (verbose handshake tracing) — to isolate 5 self-engineered failure scenarios, including slow-to-resolve vs slow-to-respond root causes.
2. **From-Memory Networking Cheat Sheet:** Wrote a 1-page consolidation of the entire week (OSI layers, subnetting/CIDR math, DNS record types, L4 vs L7 load balancing, TLS handshake) from pure recall, then patched the gaps against notes.