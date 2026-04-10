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
**Programming Language**| Python 3 (raw sockets -linux or scapy -windows)
**Log Ingestion** | Kafka
**API** | FastAPI
**Storage** | OpenSearch
**Machine learning** | numpy, scikit-learn (Isolation Forest)
**Log Ingestion** | Kafka
**Sen

# Getting Started 📦
- 
