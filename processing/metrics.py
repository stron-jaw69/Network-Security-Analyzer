# processing/metrics.py

import time
from collections import defaultdict

class TrafficMetrics:
    def __init__(self):
        self.reset()

    def reset(self):
        self.start = time.time()
        self.bytes = 0
        self.packets = 0
        self.ports = defaultdict(int)

    def update(self, pkt):
        self.bytes += len(pkt.get("raw", b""))
        self.packets += 1
        if pkt.get("src_port"):
            self.ports[pkt["src_port"]] += 1

    def snapshot(self):
        elapsed = max(time.time() - self.start, 1)
        return {
            "bandwidth_bps": (self.bytes * 8) / elapsed,
            "packets": self.packets,
            "ports": dict(self.ports)
        }
