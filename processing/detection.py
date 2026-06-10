# processing/detection.py

import time
from collections import defaultdict

class DoSDetector:
    def __init__(self, threshold=100):
        self.syn = defaultdict(int)
        self.threshold = threshold

    def update(self, pkt):
        flags = pkt.get("tcp_flags", 0)
        if flags & 0x002:
            ip = pkt.get("src_ip")
            self.syn[ip] += 1
            if self.syn[ip] > self.threshold:
                return {"event": "possible_syn_flood", "src_ip": ip}
