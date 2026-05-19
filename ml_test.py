from processing.ml_anomaly import MLAnomalyDetector

#instantiate the anomaly detector for testing
detector = MLAnomalyDetector()

for i in range(600):
    detector.update({"raw": b"x"*100, "src_port": 80, "dst_port": 443, "tcp_flags": 2})

event = detector.update({"raw": b"x"*2000, "src_port": 9999, "dst_port": 1, "tcp_flags": 0})
print(event)
