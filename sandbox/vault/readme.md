# 🛡️ Local SRE Secrets Vault (Persistent Credentials Store)

An interactive, text-based Python security utility designed to safely store, retrieve, and audit sensitive service credentials and API keys in-memory and persist them onto physical disk storage.

---

## 🛠️ Features & Engineering Concepts:
* **$O(1)$ Constant-Time Lookup:** Utilizes Python Dictionaries (Hash Maps) to achieve instant read/write operations regardless of the scale of stored credentials.
* **File-System Persistence (I/O stream):** Writes and loads credential databases directly to/from a local physical text file (`vault.txt`) utilizing safe file stream handlers.
* **Automated Password Audit:** Loops through all active credentials, executing string length validations to detect and flag insecure passwords (less than 8 characters).
* **Input-Sanitized Interactive CLI:** Features a persistent `while` loop menu with secure string-literal evaluations to prevent terminal crashes.

---

## 📅 How to Play/Run:
To launch your secure local vault, navigate to this directory and run:
```bash
python3 vault.py