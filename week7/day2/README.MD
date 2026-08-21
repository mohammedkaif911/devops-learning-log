# Week 7 · Day 2: First EC2 Lifecycle & BST Navigation

Today, I moved from EC2 theory to my first tightly timeboxed paid-compute lifecycle. AWS Support had confirmed that my account was not eligible for Free Tier or promotional credits, so I treated every resource as billable. I used temporary action-limited IAM permissions, launched one official Amazon Linux instance in Hyderabad, connected securely through WSL and SSH, captured runtime evidence, performed remote file I/O, terminated the instance, and audited every possible leftover. I also continued Binary Search Trees through ancestor discovery and inorder rank selection.

## What I Learned

* **EC2 Architecture:**
  * An AMI defines the operating system and initial machine image.
  * An instance type defines virtual CPU, memory, architecture, and network capacity.
  * EBS provides persistent block storage independently of compute lifecycle state.
  * Security groups are stateful, allow-only virtual firewalls.
  * A key pair uses a public key on AWS and a private key that must remain local.

* **EC2 Access and Security:**
  * SSH port 22 should be restricted to my current public IPv4 address using `/32`.
  * `0.0.0.0/0` must not be used for administrative SSH access.
  * Amazon Linux uses `ec2-user` as its standard SSH username.
  * A `.pem` private key should be stored outside Git and restricted with `chmod 400`.
  * Root should establish or recover control, while normal operations use a scoped IAM identity.

* **EC2 Lifecycle and Billing:**
  * Reboot keeps compute billing active.
  * Stop ends compute billing, but an attached EBS volume can continue charging.
  * An auto-assigned public IPv4 address is released on stop or termination.
  * Closing SSH with `exit` does not stop or terminate the instance.
  * Termination must be followed by checks for volumes, snapshots, addresses, network interfaces, security groups, and key pairs.
  * The live Hyderabad Linux price displayed for `t3.micro` was `$0.0112` per hour.
  * No Free Tier or credit allowance was assumed.

## SRE Labs Completed

1. **Paid Cost Gate:** Approved one 60–90 minute experiment with a ₹5 abort ceiling. Reviewed compute, EBS, public IPv4, data transfer, idle behaviour, teardown, and bill verification before launch.

2. **Temporary Least-Privilege Access:** Root created the action-limited `Week7Day2-Temporary-EC2-Lab` inline policy for `kaif-dev` instead of attaching `AmazonEC2FullAccess`, then signed out.

3. **Cost-Bounded EC2 Launch:** Launched one official Amazon Linux 2023 `x86_64` instance in `ap-south-2` using `t3.micro`, one 8-GiB `gp3` root volume, and one temporary auto-assigned public IPv4. No Elastic IP, Marketplace software, snapshot, additional volume, IAM instance profile, or detailed monitoring was used.

4. **Restricted SSH Access:** Created a temporary security group allowing TCP/22 only from My IP `/32`, secured the RSA `.pem` key inside WSL, and connected successfully as `ec2-user`.

5. **Runtime Evidence:** Verified all instance health checks, Amazon Linux `2023.12.20260817`, an `x86_64` kernel, approximately 1 GiB of memory, an 8-GiB root filesystem, uptime, load, and UTC time.

6. **Remote Write/Read Test:** Created and read `/home/ec2-user/week7-day2-proof.txt`. The proof line was recorded at `2026-08-21T16:56:32Z`.

7. **Termination and Residual Audit:** Terminated the instance after approximately 35–40 minutes. Confirmed that no root EBS volume, owned snapshot, Elastic IP, or lab network interface remained. Deleted the temporary security group, AWS key-pair record, both local `.pem` copies, and the temporary IAM policy.

8. **Bill Verification:** The immediate Bills view still showed ₹0, which was recorded as reporting delay rather than proof of zero cost. The estimated final lab cost is approximately ₹1–₹2, with a billing recheck scheduled for 22 August 2026.

## DSA Results

* **LeetCode #235 — Lowest Common Ancestor of a BST**
  * Independently identified the BST comparison and split-point logic.
  * Corrected the recursive-return propagation so the found ancestor reached the outer call.
  * Time: `O(H)` · Recursive space: `O(H)`.
  * **Accepted at 62 ms.**
  * Cold revisit due 23–24 August.

* **LeetCode #230 — Kth Smallest Element in a BST**
  * Independently chose inorder traversal to collect BST values in ascending order and returned `result[k - 1]`.
  * Needed one hint to invoke the helper after defining it.
  * Time: `O(N)` · List space: `O(N)` · Recursive stack: `O(H)`.
  * **Accepted at 3 ms.**
  * Cold revisit due 23–24 August.
