# Week 6 · Day 4: The Linked List Capstone & The First Tree

Today, I closed the linked list chapter with its hardest synthesis problem ever attempted, then crossed into a new data-structure species — trees — wielding recursion for the very first time. The morning opened with the Evidence Court: cold re-solves of Merge, Middle, and Remove-Nth — all three ALIVE, imposter charges dismissed.

## What I Learned:
* **LeetCode #2 - Add Two Numbers (Medium):** Digit-by-digit addition on backwards-stored lists — the reversed storage is the shortcut, units first. The carry is a traveler: `digit = total % 10` stays in the node, `total // 10` rides to the next column. Built with dummy + tail; the loop runs `while l1 or l2 or carry` — even the final overflow gets its node.
* **LeetCode #143 - Reorder List (Medium) — THE CAPSTONE:** A three-act heist fusing three conquered techniques: **find the middle** (tortoise & hare) + **cut the bridge** (`slow.next = None`), **reverse the second half**, then **the weave** — two walkers, save both futures, cross-stitch (`first.next = second`, `second.next = tmp1`), advance from the saves. Law of the weave: *first grabs second, second grabs first's future.* **Achieved 0 ms runtime, beating 100.00% of Python submissions!**
* **Tree Foundations:** Binary trees = nodes with `left`/`right` children; root, leaves, subtrees. The mental shift: trees don't WALK — they DELEGATE. Recursion is their native tongue.
* **LeetCode #104 - Maximum Depth of Binary Tree:** My first recursive program — base case (None → 0), recursive law: *depth = 1 + the deeper child's depth.* **0 ms runtime, beating 100.00%!**

## SRE Labs Completed:
1. **ghinfo v2 — TTL Caching Layer (shipped to `devops-toolkit`):** Built a 60-second time-to-live cache — reader checks file existence + age, fresh hits served with ZERO API calls, stale hits refetched and overwritten. My first tool published in my new toolkit repo. ⚡