import pika
import json
import threading

from typing import Callable, Dict, Any

from ...core.ports.message_broker_port import MessageBrokerPort

class RabbitMQMessageBrokerDriver(MessageBrokerPort):
  _connection = None

  def __init__(self, host: str) -> None:
    self.host = host
    self.connection = None

    if not RabbitMQMessageBrokerDriver._connection:
      RabbitMQMessageBrokerDriver._connection = pika.BlockingConnection(pika.ConnectionParameters(host=host))
    self.connection = RabbitMQMessageBrokerDriver._connection
  
  
  def subscribe_topic(self, exchange: str, route: str, callback: Callable[[bytes], None]) -> None:
    def consume_messages():
      channel = self.connection.channel()
      channel.exchange_declare(exchange=exchange, exchange_type='direct')
      
      result = channel.queue_declare(queue='', exclusive=True)
      queue_name = result.method.queue
      
      def subs_callback(ch, method, properties, body):
        callback(json.loads(body.decode('utf-8')))
      
      channel.queue_bind(exchange=exchange, queue=queue_name, routing_key=route)
      channel.basic_consume(queue=queue_name, on_message_callback=subs_callback, auto_ack=True)
      channel.start_consuming()
      
    thread = threading.Thread(target=consume_messages, daemon=True)
    thread.start()

  
  def publish_message(self, exchange: str, route: str, data: Dict[str, Any]) -> None:
    message_body = json.dumps(data)
    channel = self.connection.channel()
    
    channel.exchange_declare(exchange=exchange, exchange_type='direct')
    channel.basic_publish(exchange=exchange, routing_key=route, body=message_body)
    
    
  def close(self) -> None:
    if self.connection:
      self.connection.close()
      RabbitMQMessageBrokerDriver._connection = None