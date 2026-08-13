# Week 6 · Day 2: The requests Automation Era & Floyd's Legendary Hare

Today, HTTP became code: I mastered Python's requests library end-to-end, shipped a live three-API automation script with full error guarding, and conquered two linked list problems — including the most famous cycle-detection algorithm in computer science.

## What I Learned:
* **Python `requests` Library (full automation stack):**
  * **GET & the Response object:** one call returns the entire delivery — `status_code`, `headers`, raw `text`, and parsed `json()` (false→False, null→None on entry).
  * **Query parameters:** `params={...}` dicts auto-build the query string — no hand-assembled `?` chains.
  * **POST + 201 Created:** `json=payload` writes the body AND stamps Content-Type; the server issues the newborn resource its `id` — its address for life.
  * **Error guarding:** requests hands back 404s *silently* — `raise_for_status()` + `try/except` is the law of production scripts.
  * **Auth headers:** `headers={"Authorization": "Bearer <token>"}` — the stateless ID card, attached in code.
* **Revision Gate Passed:** POST creates · PUT replaces the whole body at the same address · PATCH updates selected fields.
* **LeetCode #21 - Merge Two Sorted Lists:** Dummy sentinel + walking tail — compared fronts, spliced winners in O(1) space, attached the sorted survivor whole. **Achieved 0 ms runtime, beating 100.00% of Python submissions!**
* **LeetCode #141 - Linked List Cycle:** Deployed Floyd's Tortoise & Hare — 1-step vs 2-step runners; on a closed track, the hare always laps the tortoise. O(N) time, O(1) space: provably optimal.

## SRE Labs Completed:
1. **Three-API Live Data Script:** Built one guarded Python script calling a joke API, CoinGecko (BTC→INR via params), and Open-Meteo (Bengaluru weather, nested-key extraction) — each with raise_for_status + try/except. Observed live-state drift between runs (BTC price moved), proving APIs serve the world's current state.
2. **Silent-Failure Bug Hunt:** Caught a guard named but never executed (`raise_for_status` missing parentheses) — law learned: naming a function does nothing; calling it does the work.