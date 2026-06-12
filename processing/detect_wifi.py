# processing/detect_wi-fi.py
from collections import defaultdict
import time

class WiFiAnomalyDetector:
    def __init__(self, probe_threshold=50):
        self.probes = defaultdict(int)
        self.last_reset = time.time()
        self.probe_threshold = probe_threshold
        self.known_bssids = set()  # Add your real AP BSSIDs here

    def update(self, pkt):
        wifi = pkt.get("wifi")
        if not wifi:
            return None
        # detect probe floods
        if wifi["addr1"] == "ff:ff:ff:ff:ff:ff":  # broadcast
            src = wifi["addr2"]
            self.probes[src] += 1

            if self.probes[src] > self.probe_threshold:
                return {"event": "wifi_probe_flood", "src_mac": src}

        # detect rogue APs
        bssid = wifi["addr3"]
        if bssid not in self.known_bssids:
            return {"event": "rogue_ap_detected", "bssid": bssid}