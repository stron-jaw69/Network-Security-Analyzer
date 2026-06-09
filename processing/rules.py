# netsec_analyzer/processing/rules.py
from typing import Dict, Any, List
def suggest_controls(event: Dict[str, Any]) -> List[str]:
    suggestions = []

    if event.get("event") == "wifi_probe_flood":
        suggestions.append("Investigate devices sending excessive probe requests.")
        suggestions.append("Enable band steering and reduce probe response load.")

    if event.get("event") == "rogue_ap_detected":
        suggestions.append("Check for unauthorized access points broadcasting your SSID.")
        suggestions.append("Enable AP isolation and monitor channel overlap.")

    if event.get("event") == "possible_syn_flood":
        suggestions.append("Tighten firewall rules: rate-limit SYN packets and enable SYN cookies on edge devices.")
        suggestions.append("Place the target service behind a reverse proxy or load balancer with DoS protection.")

    if event.get("event") == "tcp_handshake_anomaly":
        suggestions.append("Inspect firewall stateful rules for incomplete connections and enable aggressive timeout.")

    if event.get("protocol") == "SMTP":
        suggestions.append("Enforce TLS for SMTP, enable spam/AV gateway, and restrict open relay behavior.")

    if event.get("protocol") == "IMAP":
        suggestions.append("Require VPN or TLS for IMAP access and restrict access by subnet.")

    if event.get("sensitive_asset", False):
        suggestions.append("Segment the network: move this asset to a protected subnet with strict ACLs.")
        suggestions.append("Use VPN for administrative access and encapsulate management traffic (e.g., IPsec).")

    return suggestions
