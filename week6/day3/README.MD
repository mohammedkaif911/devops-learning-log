# Week 6 · Day 3: My First CLI Tool & Two-Pointer Linked List Surgery

Today I crossed from using tools to BUILDING them — engineered a live, error-guarded, argparse-driven CLI tool against the GitHub API, then executed two linked list surgeries with the tortoise and the hare.

## What I Learned:
* **CLI Engineering (ghinfo):**
  * **Tool anatomy:** input → request → guard → parse → readable output. Driven by command-line ARGUMENTS, not interactive prompts — the automation-friendly way.
  * **argparse:** flags (`--user`), free `--help` screens, and clean required-argument errors before my code even runs — the same interface language as curl and git.
  * **Layered error guarding:** `HTTPError` for bad responses, `ConnectionError` for dead networks — two doors, two guards.
* **Revision Gate:** Wrote a 5-line GET script from memory — logic perfect, syntax polished on the spot.
* **LeetCode #876 - Middle of the Linked List:** The hare runs the road at double speed, so the tortoise stands at exactly half when the race ends. **Solved solo, FIRST TRY — 0 ms, beating 100.00% of Python submissions!**
* **LeetCode #19 - Remove Nth Node From End (Medium):** Head-start measuring tape (n-step gap) + dummy sentinel + one-arrow surgery. Forged the COMMENT-FIRST CODING technique mid-battle: logic as comments first, code second. **0 ms runtime, beating 100.00%!**

## SRE Labs Completed:
1. **ghinfo CLI Tool (shipped to sandbox/):** Live GitHub profile interrogation with argparse interface and dual error guards — tested across happy path, invalid user, and missing-flag scenarios.