# Week 7 · Day 1: Identity Gates, Explicit Deny & The First BST Boundaries

Today, I entered Week 7 by deepening AWS Identity and Access Management through the real identities and policies already operating inside my account. Instead of recreating an IAM user merely to satisfy the roadmap, I audited the existing `kaif-dev` setup and connected authentication, authorization, users, groups, roles, policy types, explicit-deny precedence, least privilege, and cloud-cost responsibility to evidence from previous AWS experiments. The DSA session then entered Binary Search Trees, introducing inherited validation boundaries and recursive insertion.

## What I Learned:

* **Authentication vs Authorization:**
  * Authentication proves who an identity is through credentials such as passwords, MFA, or access keys.
  * Authorization evaluates policies to decide which AWS API actions that authenticated identity may perform.
  * Successful authentication does not guarantee authorization: `kaif-dev` could enter the console while Billing remained denied.

* **IAM Users, Groups, and Roles:**
  * An IAM user is a long-term identity with optional console credentials and programmatic access keys.
  * An IAM group collects users so shared policies can be managed in one place; a group cannot log in.
  * An IAM role is temporarily assumed by a trusted person, workload, or AWS service and normally avoids permanent credentials.
  * Future Cloud Resume Lambda functions will use execution roles instead of hardcoded access keys.

* **IAM Policy Anatomy and Evaluation:**
  * Policies are JSON documents built from `Version`, `Statement`, `Effect`, `Action`, `Resource`, and optional `Condition` fields.
  * AWS begins with implicit deny.
  * A matching Allow permits an action.
  * An explicit Deny overrides every matching Allow.

* **IAM Policy Types:**
  * AWS-managed policies are created and maintained by AWS.
  * Customer-managed policies are created inside an account and can be reused.
  * Inline policies are embedded directly in one user, group, or role.
  * `AmazonS3ReadOnlyAccess` is AWS-managed, while `Day6EC2DescribeInstancesOnly` is an inline policy.

* **Principle of Least Privilege:**
  * Grant only the actions, resources, conditions, and duration required for a task.
  * The EC2 inventory lab needed only `ec2:DescribeInstances`, not `AmazonEC2FullAccess`.
  * IAM permissions themselves do not cost money; billing begins only when a billable resource or usage dimension is consumed.

* **LeetCode #98 — Validate Binary Search Tree:**
  * A valid BST must satisfy ancestor constraints across the entire subtree—not only parent-child comparisons.
  * Every node receives an inherited range: `lower < node.val < upper`.
  * Left recursion keeps the lower bound and replaces the upper bound with the current value.
  * Right recursion replaces the lower bound with the current value and keeps the upper bound.
  * Time: `O(N)` · Recursive space: `O(H)`.
  * **Accepted at 3 ms.**

* **LeetCode #701 — Insert into a Binary Search Tree:**
  * Followed BST comparisons until reaching an empty child position.
  * A `None` position returns a new `TreeNode(val)`.
  * The recursive return is assigned to `root.left` or `root.right` to reconnect the updated subtree to its parent.
  * Time: `O(H)` · Worst case: `O(N)` in a skewed tree.
  * **Accepted at 3 ms.**

* **Cold Revision — #226 Invert Binary Tree:**
  * Rebuilt the recursive solution in under five minutes without help.
  * Independently debugged multiple errors and submitted at 0 ms.
  * Moved from guided learning to cold-verified ALIVE status.

## SRE Labs Completed:

1. **Existing IAM Architecture Audit:** Classified the active `kaif-dev` identity, its AWS-managed S3 policy, its identity-specific inline EC2 policy, console password, MFA protection, and programmatic credentials without exposing any secrets.

2. **Authorization Evidence Review:** Connected real outcomes to policy evaluation: S3 allowed, Billing denied, EC2 initially denied, and EC2 inventory later allowed through one minimal action.

3. **Cloud Cost Gate:** Established a permanent pre-service checklist covering service purpose, billing dimensions, free allowance, idle cost, expected lab maximum, teardown procedure, and bill verification.

4. **Roadmap Lab Adaptation:** Reused and audited the securely configured IAM user instead of creating a duplicate identity solely to tick a curriculum checkbox.
