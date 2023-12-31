from typing import Dict
import pika
import json

class RabbitmqPublisher:
    def __init__(self) -> None:
        self.__host = "localhost"
        self.__port = 5672
        self.__username = "rabbitmq"
        self.__password = "rabbitmq"
        self.__exchange = "queue_exchange"
        self.__routing_queue = 'RK' # Usado para ter a mesma exchange em mais de uma fila (Trocar o envio das mensagens)
        self.__channel = self.__create_channel()
        
    def __create_channel(self):
        connection_params = pika.ConnectionParameters(
            host=self.__host,
            port=self.__port,
            credentials=pika.PlainCredentials(
                username=self.__username,
                password=self.__password
            )
        )

        channel = pika.BlockingConnection(connection_params).channel()  
        return channel
    
    def send_message(self, body: Dict):
        self.__channel.basic_publish(
            exchange=self.__exchange,
            routing_key=self.__routing_queue,
            body=json.dumps(body),
            properties=pika.BasicProperties(delivery_mode=2)
        )
        
        
rabbitmq_publisher = RabbitmqPublisher()
rabbitmq_publisher.send_message({"id": 1, "message": "maybe this can be a message one day"})