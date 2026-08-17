# Week 6 · Day 5: Python Enters AWS & The Recursive Tree Mirror

Today, my local Python environment crossed the cloud boundary for the first time: I securely connected boto3 to AWS, completed an authenticated S3 API call, and received a successful empty-bucket response—the blank canvas proved that the entire Python → SDK → IAM → AWS handshake worked. I then deepened my first recursion lessons by solving two binary-tree problems based on recursive subtree delegation.

## What I Learned:

* **boto3 — AWS SDK for Python:**
  * boto3 allows Python programs to communicate with AWS services through their APIs.
  * A service client such as `boto3.client("s3")` exposes operations supported by that AWS service.
  * The script contains no hardcoded access keys; boto3 obtains credentials through AWS's credential chain.

* **AWS Credential Chain & IAM Safety:**
  * boto3 found the configured IAM credentials from the shared AWS credential files inside WSL2.
  * The IAM user was restricted with S3 read-only permissions instead of receiving administrator access.
  * The local credentials file was protected with Linux permission mode `600`, allowing only the owner to read or modify it.
  * Credentials, account files, CSV keys, and secrets must never enter Git.

* **Amazon S3 Foundations:**
  * S3 is AWS object storage: buckets act as top-level containers, while objects hold data and are identified by keys.
  * My account currently contains no buckets, so the first successful response represented a clean cloud workspace.
  * Listing buckets is a read-only operation and does not create infrastructure.

* **Caching Revision:**
  * A TTL cache reuses recently fetched data instead of repeating an API request while the response is still fresh.
  * This reduces latency, unnecessary network traffic, and API rate-limit consumption.

* **LeetCode #226 — Invert Binary Tree:**
  * At every node, swapped the left and right child references, then recursively delegated the same operation to both subtrees.
  * The call-frame model initially slipped, but tracing each child as the local root of its own subtree made the recursion click.
  * Base case: a `None` node ends that branch.
  * Time: `O(N)` · Recursive space: `O(H)`.
  * **Accepted at 0 ms.**

* **LeetCode #100 — Same Tree:**
  * Compared two trees through three recursive guards: both nodes missing, only one missing, or corresponding values differing.
  * Corrected an early mistake of comparing child-node objects directly; the real answer must use the Boolean results returned by the recursive left and right comparisons.
  * Both corresponding subtrees must match, so their results are combined using `and`.
  * Time: `O(N)` · Recursive space: `O(H)`.
  * **Accepted at 0 ms.**

## SRE Labs Completed:

1. **Secure AWS CLI and boto3 Configuration:** Configured the Hyderabad region in WSL2, connected boto3 through the shared credential chain, and kept every credential outside the source code and Git repository.

2. **First Authenticated Cloud API Call:** Created an S3 client and successfully executed `list_buckets`. The empty result was expected and proved that authentication, authorization, networking, region configuration, and SDK communication were functioning correctly.

3. **Cloud Cost Guardrails:** Confirmed the zero-spend budget watchdog and deliberately avoided EC2 or other potentially billable infrastructure while the AWS credit decision remains unresolved.