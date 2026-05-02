# Network-Security-Analyzer

🛡️A monitoring tool that integrates packet capture, protocol parsing, Kafka-based log ingestion, machine-learning anomaly detection, OpenSearch analytics, and a FastAPI-driven SOC interface.
# Objectives 🎯
- **Project base:** Provide real‑time visibility for network traffic and protocol behavior
- Detect anomalies, intrusions, and DoS attempts using both rule‑based and ML‑based methods
- Correlate Zeek/Suricata logs with raw packet data
- Store events and metrics for long‑term analysis in OpenSearch
- Unify API for alerts, cases, statistics, and automated response
# Features 🖌️
- **Traffic Capture & Parsing:**
    - Raw packet capture (LAN/Wi‑Fi)
    - Protocol support: ARP, DNS, TCP, ICMP, IMAP, SMTP
    - Bandwidth, packet rate, port usage, IP statistics
- **Detection Engine:**
    - TCP handshake verification
    - SYN flood / DoS heuristics
    - Machine Learning anomaly detection (Isolation Forest)
    - Suricata/Zeek log ingestion via Kafka
- **SOAR Automation:**
    - Automated firewall blocking
    - Alerting and incident creation
    - Implement the playbook system


# Technical Stack ⚙️
 Layer | Technology 
-------|-------------
**Programming Language**| Python 3, (raw sockets -linux or scapy -windows)
**Log Ingestion** | Kafka
**API** | FastAPI
**Storage** | OpenSearch (event index and querrying)
**Machine learning** | numpy, scikit-learn (Isolation Forest)
**Log Ingestion** | Kafka
**Sensors** | Suricate, Zeek

# Getting Started 📦
### 1. **Clone the repository**
- git clone https://github.com/stron-jaw69/Network-Security-Analyzer.git
- cd Network-Security-Analyzer
### 2. **Create the virtual environment**
- **Windows:**
    - python -m venv venv
    - venv\Scripts\activate
- **Linux/mac:**
    - python3 -m venv venv
    - source venv/bin/activate
### 3. **Install dependecies**
- pip install -r requirements.txt
### 4. **Windows PreReq**
- install Npcap
- enable (winPcap API-compatible mode and RAW 802.11)
### 5. **Run FASTAPI servers**
- uvicorn api.main:app --reload
- open api doc for testing, view stats: http://127.0.0.1:8000
- access api docs: http://127.0.0.1:8000/docs
- OR: http://127.0.0.1:8000/redoc
- wireless dashboard: http://127.0.0.1:8000/wifi/dashboard
### 6. **Test Endpoints**
- SOAR: POST /soar/run
- Bandwidth: GET/ stats/bandwidth
### 7. **Test Pack Captures**
- **Windows (npcap):**
    - python capture/raw_sniffer.py
- **Linux:**
    - sudo python capture/raw_sniffer.py
### 8. **Anomaly Detection**
- Execute the first set of packets: python anomaly.py
### 9. **Test Kafka with Zeek/suricata**
- python zeek_suricata.py *
### 10. **OpenSearch indexing**
- bash: http://localhost:9200
- curl -X GET "local"
