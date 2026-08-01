# ☁️ SRE Cloud Cost & Instance Optimizer (FinOps Tool)

A lightweight, automated Cloud Financial Operations (FinOps) utility designed to parse AWS cloud instance inventories, audit active daily run costs, and identify idle servers wasting system budgets.

## 🛠️ Features & SRE Concepts:
* **Asymmetric State Auditing:** Reads and parses active AWS resource logs (`instances.txt`) using safe file-stream operations.
* **Cost Minimization Logic:** Executes conditional audits to separate running servers from stopped instances, and flags active instances running with "idle" resource metrics.
* **Auto-Scaling Preparation:** Generates a clean, actionable diagnostic report listing the exact AWS Instance IDs that should be terminated to prevent cloud budget leakage.
* **No-Global Modularity:** Built entirely using self-contained, isolated local variables and functional returns to prevent memory state-corruption.

## 📅 How to Run:
Navigate to this directory and execute the optimizer using:
```bash
python3 finops_optimizer.py