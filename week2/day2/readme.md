# Week 2 · Day 2: User Access Control & Advanced Algorithmic Sums

Today, I mastered how the operating system manages users, groups, and temporary administrative privileges, and solved advanced string slicing and collection algorithms.

## What I Learned:
* **User & Group Administration:** Mapped user databases inside `/etc/passwd` and groups inside `/etc/group`. 
* **CLI Auditing Commands:**
  - `useradd -m -s /bin/bash` provisions new users with home directories and bash shell defaults.
  - `usermod -aG` appends users to secondary groups (Crucial: omitting `-a` causes group deletion/overwrite).
  - `id` and `groups` audit active UID/GIDs globally.
* **Privilege Escalation (`visudo`):** Explored how `sudo` elevates privileges safely using `/etc/sudoers`. Discovered why standard editors like `nano` can brick sudo access, and why `visudo` checks syntax in the background before saving.
* **String Slicing:** Mastered slicing characters out of strings using brackets and colons (e.g. `s[2:-2]` to remove markers).

## Scripts Completed:
1. `HR_candle.py`: Solves "Birthday Cake Candles" utilizing array maximum counts in O(N) linear time.
2. `HR_timeconversion.py`: Converts 12-hour AM/PM timestamps to 24-hour UTC military format using string slicing.