import pika 

class RabbitMqConsumer:
    def __init__(self, callback) -> None:
        self.__host = "localhost"
        self.__port = 5672
        self.__username = "rabbitmq"
        self.__password = "rabbitmq"
        self.__queue = "queue"
        self.__callback = callback
        self.__channel = self.__create_channel()
        
    def __create_channel(self): 
        connection_params = pika.ConnectionParameters(
            host=self.__host, port=self.__port, credentials=pika.PlainCredentials(
                username=self.__username,
                password=self.__password
            )
        )
        channel = pika.BlockingConnection(connection_params).channel()
        channel.queue_declare(queue=self.__queue, durable=True)
        channel.basic_consume(
            queue=self.__queue,
            auto_ack=True,
            on_message_callback=self.__callback 
        )
            
        return channel

    def start(self):    
        print("Listening RabbiMQ on port 5672")
        self.__channel.start_consuming()
        
        
def callback(ch, method, properties, body):
    print(body)
    
rabbitmq_consumer = RabbitMqConsumer(callback)
rabbitmq_consumer.start()