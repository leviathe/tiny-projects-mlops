import json
from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers='nowledgeable.com:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8'),
)

for _ in range(10):
        producer.send('exo1', "Hello World")

producer.flush()