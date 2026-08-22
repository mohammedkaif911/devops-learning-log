# Week 7 · Day 3: Level-Order Engines and a Metered First Bucket

Today I stopped trusting "the right side of the tree" — and my first metered events
on a paid AWS account landed behind a cost gate, a six-action scoped policy, and a
teardown order. Both trees problems closed, S3 fundamentals core done, and the lab
is reproducible from the runbook.

## What I Learned

**S3 fundamentals** — a bucket is a named, globally-unique container; an object is
key + data + metadata. S3 bills three things: storage (GB-month), requests
(PUT/GET tiers), and egress (GB out) — no fixed bucket fee. The IAM quirk that
matters: bucket-level actions (CreateBucket/ListBucket/DeleteBucket) target the
bare bucket ARN, object-level actions (Put/Get/DeleteObject) target `arn:.../*` —
a scoped policy needs both lines. A non-empty bucket cannot be deleted: objects
first, then the bucket. Permission ≠ usage — attaching the policy cost $0.00; the
meter only ticked at the first PUT.

**Trees · #102 Level Order Traversal** — every recursive call carries `level`
(root = 0); a visited node drops its value into `result[level]` and hands its
children `level + 1`. Core mechanism: the list belongs to the LEVEL, not the node
— one list per level, created by the first arrival (`level == len(result)`),
appended by everyone after. DFS reaches levels in order, so `==` suffices.
O(n) time, O(n) result, O(h) stack.

**Trees · #199 Right Side View** — the visible node per level is the last one in
left-to-right order. Trap I caught myself: the right side view is NOT the right
spine — a left-side node can be its level's rightmost node when the left goes
deeper. Engine: #102's per-level lists + `lvl[-1]` per level. O(n) time/space.

**Honest DSA results** — #102: accepted, 2 ms; two self-debugged attempts
(`list.append` arity TypeError, then an `insert` that split level lists) before a
2-line blueprint for the level-creation mechanism; cold re-solve 24–25 Aug.
#199: accepted, 0 ms; attempt 1 was a right-spine walk that missed the deepest
left node on the classic example; I stated the trap in plain English before the
fix; cold re-solve 25–26 Aug.

## SRE Labs Completed

1. **S3 first-bucket lab** (ap-south-2, identity `kaif-dev`, cost-gated, expected < $0.001)
   - Scoped temp policy (6 S3 actions on bucket ARN + `/*`) → attach → root signed out
   - `aws s3 mb` → 49-byte object uploaded (PUT + storage = first metered events)
   - `ls` + `cp` download + `cat` → byte-for-byte round-trip (server-stamped 17:29:58)
   - Ordered teardown: `rm` object → `rb` bucket → detach + delete policy
   - **Engineering lessons:** teardown order is law — non-empty buckets refuse to die;
     scope = blast radius (6 actions, 2 ARNs, nothing else); billing lags 12–24 h, so the
     receipt is observed, not assumed; "near-zero at this scale" is a different sentence
     from "free". Observed cost: pending (delayed billing, to be confirmed on next check).