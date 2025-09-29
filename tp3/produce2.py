import json
from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers='nowledgeable.com:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8'),
)

data = [
    [1, 2],
    [3, 4],
]

producer.send('Pazart', data)

producer.flush()