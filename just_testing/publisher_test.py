import pika

connection_params = pika.ConnectionParameters(
    host="localhost",
    port=5672,
    credentials=pika.PlainCredentials(
        username="rabbitmq",
        password="rabbitmq"
    )
)

channel = pika.BlockingConnection(connection_params).channel()

channel.basic_publish(
    exchange="queue_exchange",
    routing_key="",
    body="this is probably a message",
    properties=pika.BasicProperties(delivery_mode=2)
)