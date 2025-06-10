# ⚡ Port Hunter

A fast, asynchronous port scanner built for red teamers, bug bounty hunters, and cyber operators.  
Developed by [RootStrike](https://github.com/ROOTSTRIKE) — tuned for stealth, speed, and results.

---

## 🔥 Features

- Asynchronous scanning (fast + efficient)
- Supports custom ports or full ranges
- Timeout & sleep delay to reduce detection
- Lightweight, no external dependencies
- Designed for operational recon & bug bounty

---

## 📦 Installation

```bash
git clone https://github.com/ROOTSTRIKE/port-hunter.git
cd port-hunter
pip install -r requirements.txt
⚠️ Requires Python 3.7+

🚀 Usage
bash
Copy
Edit
python3 port_hunter.py -iL targets.txt -p 22,80,443 -t 1 -s 0.2
Flag	Description
-iL	Input file with target IPs
-p	Ports (comma-separated or range)
-t	Timeout per port (sec)
-s	Sleep between scans (sec)
-c	Concurrency (default: 100)

📁 Sample targets.txt
txt
Copy
Edit
127.0.0.1
scanme.nmap.org
🧠 Why Port Hunter?
💨 Async = speed with stealth

🥷 Small footprint, avoids floods

⚔️ Ideal for initial recon and passive scans

💡 Great starter tool for red team workflows


🧠 Built By
RootStrike — Cyber Ops, OffSec, Recon Tools
🔗 github.com/ROOTSTRIKE

