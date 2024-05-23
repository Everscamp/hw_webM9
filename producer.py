import faker
from models import Contact
from connect import client
import pika
import json


fake_data = faker.Faker()
db = client.test

credentials = pika.PlainCredentials('guest', 'guest')
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
channel = connection.channel()

channel.exchange_declare(exchange='task_mock', exchange_type='direct')
channel.queue_declare(queue='task_queue', durable=True)
channel.queue_bind(exchange='task_mock', queue='task_queue')


def main():
    for i in range(10):
        name = fake_data.name()
        email = fake_data.email()
        Contact(fullname=name, email=email, is_sent=False).save()

        contact_id = db.contact.find_one({'fullname': name}).get('_id')

        message = {"id": str(contact_id)}

        channel.basic_publish(
            exchange='task_mock',
            routing_key='task_queue',
            body=json.dumps(message).encode(),
            properties=pika.BasicProperties(
                delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
            ))
        print(" [x] Sent %r" % message)
    connection.close()
    
    
if __name__ == '__main__':
    main()