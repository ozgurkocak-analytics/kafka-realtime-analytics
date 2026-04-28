import json
import time
import uuid
import random
import os
from confluent_kafka import Producer
from dotenv import load_dotenv

# .env yükle
load_dotenv()

# config
conf = {
    'bootstrap.servers': os.getenv("BOOTSTRAP"),
    'security.protocol': 'SASL_SSL',
    'sasl.mechanisms': 'PLAIN',
    'sasl.username': os.getenv("API_KEY"),
    'sasl.password': os.getenv("API_SECRET"),
    'client.id': 'order-producer'
}

producer = Producer(conf)

def delivery_report(err, msg):
    if err:
        print(f"❌ Failed: {err}")
    else:
        print(f"✅ Sent to {msg.topic()} [{msg.partition()}]")

# kaç event
TOTAL_EVENTS = 500

for i in range(TOTAL_EVENTS):
    order = {
        "order_id": str(uuid.uuid4()),
        "user_id": f"user_{random.randint(1,100)}",
        "product_id": f"product_{random.randint(1,20)}",
        "price": round(random.uniform(10, 200), 2),
        "quantity": random.randint(1, 3),
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
    }

    producer.produce(
        topic=os.getenv("TOPIC"),
        key=order["user_id"].encode("utf-8"),
        value=json.dumps(order).encode("utf-8"),
        callback=delivery_report
    )

    producer.poll(0)
    time.sleep(0.2)

producer.flush()

print("🎉 Finished sending events")