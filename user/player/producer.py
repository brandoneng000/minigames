import pika
from decouple import config

params = pika.URLParameters(config('CLOUDAMQP'))

connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish():
    channel.basic_publish(exchange='', routing_key='user', body='hello')

