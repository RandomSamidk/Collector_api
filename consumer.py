from kafka import KafkaProducer, KafkaConsumer
import json 

producer = KafkaProducer(bootstrap_servers='localhost:9092')
consumer = KafkaConsumer(
    'collect-topic1',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='latest',
    enable_auto_commit=True
)

for message in consumer:
    decoded = message.value.decode('utf-8')
    data = json.loads(decoded)
    print('...Received')
    for event in data['events']:
        transformed = {
            "event_type": event['event_type'],
            "event_time":int(event['event_time']),
            "user_id": int(event['user_id']),
            "browser": data['ctx']['browser'],
            "device": data['ctx']['device']
        }
        row = json.dumps(transformed).encode('utf-8')
        producer.send("collect-topic2",value=row)
        print(row)

producer.flush()