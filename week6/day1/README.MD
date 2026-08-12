# Week 6 · Day 1: REST API Architecture & The First Linked List Conquest

Today, I opened the automation era: mastered REST architecture end-to-end through seven disciplined rungs, interrogated a live production API, and broke through my first-ever linked list problem after building the data structure from scratch on paper.

## What I Learned:
* **REST API Architecture (7-rung mastery):**
  * **API & REST:** An API is the contract that lets software talk; REST treats all data as *resources* identified by URLs — the server transfers *representations* of their state, never the resources themselves.
  * **Endpoints:** Nouns only — `/students` (collection) vs `/students/42` (item); anatomy of scheme, host, path, and query parameters.
  * **HTTP Methods & Idempotency:** The CRUD map (GET/POST/PUT/PATCH/DELETE) and why retry-safety matters — a retried POST can double-charge; a retried PUT is harmless.
  * **Statelessness:** The server remembers nothing between requests — which is exactly why it scales by simply adding machines, and why auth tokens must travel with every call.
  * **JSON Anatomy:** Two structures (objects, arrays), six value types, three strict laws.
  * **Headers:** The envelope around the letter — Content-Type declares the body's language, Content-Length marks its end; nothing assumed, everything labeled.
  * **Auth Tokens & JWT:** Bearer semantics, the header.payload.signature anatomy, and the law that a JWT payload is *encoded, not encrypted* — never store secrets inside.
* **TLS Revision Gate:** Passed from memory — TLS kills three attacks: eavesdropping (encryption), man-in-the-middle impersonation (certificates), and tampering (integrity checks).
* **LeetCode #150 - Evaluate Reverse Polish Notation:** The stack became the calculator — push numbers, pop two on operators, push results; conquered LIFO operand order and toward-zero truncation. **Achieved 0 ms runtime, beating 100.00% of Python submissions!**
* **LeetCode #206 - Reverse Linked List:** My FIRST linked list — built the mental model from raw nodes (tail-first construction, traversal, pointer surgery), then executed the three-pointer reversal: save the bridge, flip the arrow, advance. **Achieved 0 ms runtime, beating 100.00% of Python submissions — three consecutive 100% kills!**

## SRE Labs Completed:
1. **Live API Interrogation:** Performed GET calls against `api.github.com` with `curl`, inspected status line, Content-Type and cache-control headers, verified JSON body types, and observed the live rate-limit machinery (`x-ratelimit-limit: 60` / `remaining` decrementing per request).