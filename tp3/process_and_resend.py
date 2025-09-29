import json
import numpy as np
from kafka import KafkaConsumer, KafkaProducer

consumer = KafkaConsumer(
    'raw',
    bootstrap_servers='nowledgeable.com:9092',
    value_deserializer=lambda x: x.decode('utf-8')
)

producer = KafkaProducer(
    bootstrap_servers='nowledgeable.com:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8'),
)

for message in consumer:
    data = json.loads(message.value)
    sum = np.array(data).sum()
    producer.send('processed', sum)
    producer.flush()