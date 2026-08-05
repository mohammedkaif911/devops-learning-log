# Week 4 · Day 4: OOP Inheritance & Dual-Map Algorithm Plumbings

Today, I mastered the inheritance boundaries of Object-Oriented Programming (OOP) architectures, analyzed bidirectional HashMap routing, and optimized hardware register loops.

## What I Learned:
* **OOP Inheritance:** Developed hierarchical class networks. Mapped how a Child Class inherits all attributes and methods automatically from a Parent Class, and how the `super().__init__()` constructor bridge executes.
* **The Direction of Inheritance:** Documented that parent classes can never access child-specific methods, enforcing structural access controls natively.
* **LeetCode #205 - Isomorphic Strings:** Engineered a bidirectional mapping validation pipeline using two distinct dictionaries (`map_st` and `map_ts`) to block character collisions in $O(1)$ lookup time.
* **LeetCode #509 - Fibonacci Number:** Bypassed the slow $O(2^N)$ recursion trap by writing an iterative $O(N)$ time and $O(1)$ space loop, leveraging parallel tuple assignments to compute values directly inside the hardware registers.

## Custom Projects & Scripts Completed:
* `sandbox/bank_account/bank_account.py` (Moved to sandbox): Encapsulates account states and implements structural balance validation methods.