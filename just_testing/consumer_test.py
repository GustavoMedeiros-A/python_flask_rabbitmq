import pika


def callback(ch, method, properties, body):
    print(body)

connection_params = pika.ConnectionParameters(
    host="localhost",
    port=5672,
    credentials=pika.PlainCredentials(
        username="rabbitmq",
        password="rabbitmq"
    )
)

channel = pika.BlockingConnection(connection_params).channel()
channel.queue_declare(
    queue="order",
)
channel.basic_consume(
    queue="order",
    auto_ack=True,
    on_message_callback=callback
)

print("Listening RabbiMQ on port 5672")
channel.start_consuming()