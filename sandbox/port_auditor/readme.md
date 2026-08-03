# 📡 SRE Port Auditor CLI Utility

A lightweight command-line interface (CLI) automation tool designed to receive network ports directly from terminal arguments, audit their security parameters, and flag unencrypted data-transit vulnerabilities.

## 🛠️ Features & SRE Concepts:
* **Dynamic CLI Argument Parsing:** Leverages Python's native `sys.argv` array to capture and process inputs passed directly from the shell terminal.
* **Proactive Index Crash-Shield:** Implements script-level boundary validations to verify argument lengths BEFORE executing list reads, completely neutralizing fatal `IndexError` exceptions.
* **Secure Port Evaluation:** Scans and audits network ports, flagging standard cleartext protocols (HTTP 80/8080) vs. encrypted administration tunnels (SSH 22/2220).

## 📅 How to Run:
Navigate to this directory and run the auditor, passing your target port:
```bash
python3 port_auditor.py 2220