# port-hunter
⚡ Fast, async port scanner for red team recon | By RootStrike



A fast, asynchronous port scanner built for red team recon and stealthy enumeration.

---

## 🔥 Features
- Mass host scanning via async sockets
- Custom port range or full scan
- Timeout + sleep delay to reduce detection
- Easy CLI usage
- Lightweight and fast

---

## 🚀 Usage

```bash
python3 port_hunter.py -iL targets.txt -p 22,80,443 -t 0.5 -s 0.2


| Option | Description               |
| ------ | ------------------------- |
| `-iL`  | Input list of IPs/domains |
| `-p`   | Ports to scan             |
| `-t`   | Timeout (in seconds)      |
| `-s`   | Sleep between scans       |


## 📦 Installation

```bash
git clone https://github.com/ROOTSTRIKE/port-hunter.git
cd port-hunter
pip install -r requirements.txt
