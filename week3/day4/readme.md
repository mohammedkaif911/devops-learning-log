# Week 3 · Day 4: Git Branching, Conflict Resolution, & Advanced Two-Pointer Squeezing

Today, I mastered parallel repository branches, ran active local merge conflict simulations, and successfully engineered two highly complex LeetCode Medium algorithms.

## What I Learned:
* **Git Branching & Scopes:** Parallel branches are isolated sandboxes to safely test code without corrupting the stable `main` production branch.
* **The Direction of the Merge:** To pull branch code into `main`, administrators must be standing inside the destination branch first (`git checkout main`) before executing `git merge`.
* **Merge Conflicts & Resolution:** Triggered when two independent commits attempt to modify the exact same line of the same file. Git halts, injects markers (`<<<<<<<`, `=======`, `>>>>>>>`), and awaits manual intervention. Mastered manual conflict resolution, selecting target lines, and committing clean history.
* **LeetCode #11 - Container With Most Water:** Designed a boundary-squeezing two-pointer algorithm. By sliding the pointer pointing to the shorter wall inward, the program calculates maximum volumes in $O(N)$ linear time.
* **LeetCode #15 - 3Sum:** Solved an $O(N^2)$ medium-tier three-pointer sum-reduction algorithm. Locked a base index `nums[i]` and executed Two Sum II squeezes on the remaining array space, utilizing double-pointer skip checks to cleanly prevent duplicate triplets.

## Scripts & Tools Completed:
1. `LC_container_water.py`: Solves LeetCode #11 using optimized wall squeezes.
2. `LC_three_sum.py`: Solves LeetCode #15 using modular base loops and boundary squeezes.
3. `drill/website.txt`: Active sandbox representing a resolved Git merge collision.