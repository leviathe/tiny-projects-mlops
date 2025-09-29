import json
import numpy as np
from kafka import KafkaConsumer

consumer = KafkaConsumer(
    'Pazart',
    bootstrap_servers='nowledgeable.com:9092',
    value_deserializer=lambda x: x.decode('utf-8')
)
for message in consumer:
    data = json.loads(message.value)
    arr = np.array(data)
    print(np.sum(arr))