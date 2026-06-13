# zeek_suricata_consumer.py

from kafka import KafkaConsumer
import json
from config import KAFKA_BOOTSTRAP

def consume(topic):
    consumer = KafkaConsumer(
        topic,
        bootstrap_servers=KAFKA_BOOTSTRAP,
        value_deserializer=lambda m: json.loads(m.decode())
    )
    for msg in consumer:
        yield msg.value
