import pika
from pika import channel

# establishing connection with RabbitMQ server
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# create queue
channel.queue_declare(queue='hello')

# RabbigMA messages always needs to go through an exchange
# Default exchange is an empty string
# The exchange allows us to specify exactly which queue the message should go
# The queue name needs to be specified in the routing_key parameter
channel.basic_publish(
    exchange='',
    routing_key='hello',
    body='Hello World!'
)
print(" [x] Sent 'Hello World!'")

connection.close()
