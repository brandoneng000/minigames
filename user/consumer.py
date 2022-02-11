import pika
from decouple import config

params = pika.URLParameters(config('CLOUDAMQP'))

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='user')

def callback(ch, method, properties, body):
    print("Received in user")
    print(body)

channel.basic_consume(queue='user', on_message_callback=callback)

print('Started consuming')

channel.start_consuming()

channel.close()