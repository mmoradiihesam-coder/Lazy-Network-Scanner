 
# 🕵️‍♂️ Lazy Network Scanner v1.0

A lightweight, automated network reconnaissance script written in Python3 that utilizes Nmap to discover active hosts within a local subnet. Designed specifically for security auditing in Linux environments (Kali Linux).

## 🚀 Features
* **Privilege Check:** Ensures the script runs with root privileges (`sudo`).
* **Clean Output:** Filters Nmap's verbose output using `grep` and `awk` to display only live IP addresses.
* **Logging:** Automatically logs discovered hosts into a `live_hosts.txt` file.

## 🛠️ Requirements
* Linux (Kali Linux, Ubuntu, Debian, etc.)
* Python 3.x
* Nmap installed (`sudo apt install nmap`)

## 💻 Usage
Clone the repository or download the script, then run:

```bash
sudo python3 lazy_scan.py
