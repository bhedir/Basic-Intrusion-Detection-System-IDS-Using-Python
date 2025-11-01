# 🛡️ Système IDS Basique — Intrusion Detection System in Python

![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-Framework-lightgrey?logo=flask)
![Scapy](https://img.shields.io/badge/Scapy-Network%20Analysis-orange)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

## 👩‍💻 Author
**Hadir Ben Arbia**  
🎓 Cybersecurity Engineering Student — Polytechnique Sousse  
📧 hadir.benarbia@polytechnicien.tn   
📅 *November 1, 2025*

---

## 🧠 Project Overview

This project aims to design and implement a **basic Intrusion Detection System (IDS)** using Python.  
The system analyzes network traffic to detect anomalies such as:
- Unauthorized port usage  
- Excessive packet transmission from a single IP  
- Suspicious network behaviors  

All detected anomalies are recorded in log files and visualized through a **real-time Flask web interface**.

---

## 🎯 Objectives

- Capture and analyze live network packets  
- Identify abnormal patterns in the traffic  
- Log anomalies into a centralized log file  
- Visualize detection results in real-time through a web dashboard  

---

## 🧩 Technical Environment

| Component | Description |
|------------|-------------|
| **Operating System** | Linux (Kali) |
| **Language** | Python 3.10 |
| **Libraries Used** | `scapy`, `flask`, `requests` |

---

## ⚙️ Installation Guide

```bash
# Update system
sudo apt update

# Install Python environment
sudo apt install python3-pip python3-venv

# Create and activate a virtual environment
python3 -m venv env
source env/bin/activate

# Install required libraries
pip install scapy flask requests
```
## 🧠 System Architecture

### 1️⃣ Initialization

- Imports required libraries (`scapy`, `argparse`, `logging`, etc.)
- Defines authorized ports: **80**, **443**, **53**
- Initializes counters for IP packet tracking

---

### 2️⃣ Packet Analysis

Each packet is inspected through the `analyze_packet()` function:

- Checks source and destination IP and ports  
- Counts packet flow from each IP  
- Detects excessive or unauthorized traffic  
- Anomalies are logged in **`anomalies.log`**

---

### 3️⃣ Traffic Capture

- Real-time capture via Scapy’s `sniff()`  
- Offline `.pcap` file analysis  
- Graceful exit with **Ctrl + C**

---

## 🌐 Flask Web Interface

The web interface developed with **Flask** allows **real-time monitoring** of detected anomalies.

### Features:
- 🔁 **Auto-refresh every 10 seconds**  
- 🔍 **Search and filter by IP, port, or keyword**  
- 💡 **Lightweight and responsive UI**  
- 📊 **Clear visualization of logs and alerts**

> This makes the IDS accessible even to non-technical users and ideal for educational, testing, or SOC environments.

---

## 🧪 Test Scenarios

| Test Case | Description |
|------------|-------------|
| **HTTP/HTTPS Authorized Traffic** | Simulates normal web browsing traffic |
| **Port Scan Simulation** | Triggers alerts for non-authorized ports |
| **Excessive Traffic Simulation** | Detects high packet flow from one IP |

---

## 📊 Example of Output

**Sample anomaly log (`anomalies.log`):**
[INFO] Authorized port detected: 443
[WARNING] Unauthorized source port: 59987 from 192.168.1.10
[ALERT] High traffic detected from IP: 192.168.1.10 (105 packets)

**Example Packet Analysis:**
- ✅ Legitimate packet → port **443** (HTTPS)  
- ⚠️ Suspicious packet → port **59987** (unauthorized)

---

## 🚀 Future Improvements

- 🔗 Integration with **SIEM systems** (e.g., Wazuh, ELK)  
- 📧 **Email or webhook alerts** for critical detections  
- 🔐 **User authentication** on the web interface  
- 🧬 **Machine learning–based anomaly classification**

---

## 🧩 Conclusion

This project demonstrates how a lightweight **Python-based IDS** can effectively detect and log suspicious network activity.  
With **real-time monitoring**, **logging**, and a **Flask-based web interface**, it lays the foundation for more advanced intrusion detection and threat response systems.

---

## 🎥 Demo Video

📎 [Watch the project simulation on Google Drive](https://drive.google.com/file/d/1IqkmydSYEKnRaWYCVlbOvY74OAEVK88Q/view?usp=drive_link)

---

⭐ **If you found this project helpful, give it a star and share it with others!**
