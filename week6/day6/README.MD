# Week 6 · Day 6: Denied by Design & The Least-Privilege EC2 Audit

Today, I consolidated the AWS automation foundations of Week 6 by tracing boto3's credential chain, separating browser authentication from programmatic credentials, and hardening both root and IAM console access with MFA. I then turned an expected EC2 authorization failure into a least-privilege experiment: the same boto3 call moved from `UnauthorizedOperation` to a successful empty response after granting exactly one read-only permission. The DSA session completed the week's first tree chapter with inorder traversal and recursive mirror comparison.

## What I Learned:

* **boto3 Credential Provider Chain:**
  * boto3 does not operate without credentials; it loads them from external credential providers instead of requiring secrets inside source code.
  * The default profile in `~/.aws/credentials` supplied the IAM access keys, while `~/.aws/config` supplied the Hyderabad region.
  * Each AWS API request is signed using the loaded credentials.

* **Console Authentication vs Programmatic Authentication:**
  * AWS Console access uses a username, password, and MFA.
  * CLI and boto3 access use credentials discovered through the provider chain.
  * A browser logout does not disconnect CLI or boto3 sessions.
  * Root is reserved for account-level administration; the least-privilege IAM user is used for daily learning.

* **IAM Least Privilege:**
  * AWS denied `ec2:DescribeInstances` because the IAM user initially had only S3 read-only access.
  * Added an inline policy permitting only `ec2:DescribeInstances`.
  * The policy cannot launch, start, stop, modify, or terminate EC2 resources.
  * S3 access succeeded while Billing access was denied, confirming that policy boundaries were working.

* **Python Virtual Environments:**
  * The system Python environment could not import boto3 because the package was installed only inside the isolated virtual environment.
  * Activating the environment changed the available Python dependencies without modifying the global installation.

* **LeetCode #94 — Binary Tree Inorder Traversal:**
  * Used recursive depth-first traversal in the order Left → Root → Right.
  * Created one shared result list and a nested helper that recursively visited each subtree.
  * Time: `O(N)` · Recursive space: `O(H)`.
  * **Accepted at 0 ms.**

* **LeetCode #101 — Symmetric Tree:**
  * Compared two nodes at a time using mirrored outside and inside pairs.
  * Outside: `left.left` with `right.right`.
  * Inside: `left.right` with `right.left`.
  * Both recursive comparisons must succeed.
  * Time: `O(N)` · Recursive space: `O(H)`.
  * **Accepted at 0 ms.**

## SRE Labs Completed:

1. **AWS Human-Access Hardening:** Enabled separate MFA protection for the root and IAM identities, enabled IAM console access, returned root to administrative-only use, and validated routine access through the least-privilege user.

2. **Dependency Isolation Test:** Ran the EC2 script outside the virtual environment and observed that boto3 was unavailable. Activated the project environment and confirmed that Python could import boto3 and reach AWS.

3. **Deny-Then-Allow IAM Experiment:** Called `DescribeInstances` before permission and received the expected `UnauthorizedOperation`. Added the minimal `ec2:DescribeInstances` inline permission and reran the unchanged script successfully.

4. **Read-Only EC2 Inventory:** Received `EC2 reservations: []` from the Hyderabad region, proving successful authentication and authorization while creating no EC2 instances or compute charges.