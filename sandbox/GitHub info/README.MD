# 🪪 ghinfo — GitHub Profile Card Fetcher

A lightweight CLI tool that interrogates the public GitHub REST API and
prints a clean, readable profile card for any user — with full error
guarding and a proper command-line interface.

## ⚙️ Features
* Live `GET` call to `api.github.com/users/<username>` via the **requests** library
* Full error guarding: `HTTPError` (invalid user) + `ConnectionError` (network down)
* Real CLI interface via **argparse** — `--user` flag, auto-generated `--help`,
  and clean "required argument" errors when the flag is missing

## 🚀 Usage
```bash
python3 ghinfo.py --user <username>
python3 ghinfo.py --help

Example Output:
Name :  Mohammed Kaif
Bio :  Learner
Repos :  5
Followers :  1
Joined :  2026-06-02T12:44:25Z