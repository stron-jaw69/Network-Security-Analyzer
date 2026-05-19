import numpy as np
from sklearn.ensemble import IsolationForest

# Machine learning anomaly detector using Isolation Forest on packet features
class MLAnomalyDetector:
    def __init__(self):
        self.model = IsolationForest(contamination=0.01)
        self.buffer = []
        self.trained = False

    def extract(self, pkt):
        # Convert packet fields into a numeric feature vector
        return [
            len(pkt.get("raw", b"")),
            pkt.get("src_port", 0),
            pkt.get("dst_port", 0),
            pkt.get("tcp_flags", 0)
        ]

    def update(self, pkt):
        feat = self.extract(pkt)
        self.buffer.append(feat)

        if len(self.buffer) >= 500 and not self.trained:
            # Train the model when enough packets have been collected
            self.model.fit(np.array(self.buffer))
            self.trained = True

        if not self.trained:
            return None

        score = self.model.decision_function([feat])[0]
        if score < -0.2:
            # Return an anomaly event when the score is below threshold
            return {"event": "ml_anomaly_detected", "score": float(score)}
