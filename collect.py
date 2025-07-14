from kafka import KafkaProducer
from models import DataObj
import json

producer = KafkaProducer(bootstrap_servers='localhost:9092')

def collect_func(event: DataObj):
    message = json.dumps(event.dict()).encode('utf-8')
    producer.send('collect-topic1',value=message)
    print(message)
