def block_ip(event):
    ip = event.get("src_ip")
    print(f"[SOAR] Blocking IP: {ip}")

def notify(event):
    print(f"[SOAR] Alerting on-call: {event}")

PLAYBOOKS = {
    "possible_syn_flood": [block_ip, notify],
    "ml_anomaly_detected": [notify]
}

def run_playbook(event):
    for action in PLAYBOOKS.get(event["event"], []):
        action(event)
