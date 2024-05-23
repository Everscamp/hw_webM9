import pika
from connect import client
import time
import json
from mongoengine.fields import ObjectId

db = client.test

credentials = pika.PlainCredentials('guest', 'guest')
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)
print(' [*] Waiting for messages. To exit press CTRL+C')

def stub_function(message):
    email = db.contact.find_one({'_id':ObjectId(message.get('id'))}).get('email')
    return f'Email was sent to the {email}!'

def callback(ch, method, properties, body):
    message = json.loads(body.decode())
    print(f" [x] Received {message}")
    if len(stub_function(message)) != 0:
        print(f" [x] {stub_function(message)}")
        db.contact.update_one({"_id": ObjectId(message.get('id'))}, {"$set": {"is_sent": True}})

    time.sleep(1)
    print(f" [x] Done: {method.delivery_tag}")
    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='task_queue', on_message_callback=callback)


if __name__ == '__main__':
    channel.start_consuming()