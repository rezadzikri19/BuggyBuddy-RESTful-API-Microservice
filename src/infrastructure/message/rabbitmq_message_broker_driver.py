import pika
import json
import threading

from typing import Callable, Dict, Any

from ...core.ports.message_broker_port import MessageBrokerPort

class RabbitMQMessageBrokerDriver(MessageBrokerPort):
  def __init__(
      self,
      host: str,
      port: str,
      username: str,
      password: str) -> None:
    self.host = host
    self.port = port
    self.username = username
    self.password = password
  
  
  def subscribe_topic(self, exchange: str, route: str, callback: Callable[[bytes], None]) -> None:
    def consume_messages():
      credentials = pika.PlainCredentials(username=self.username, password=self.password)
      connection_params = pika.ConnectionParameters(host=self.host, port=self.port, credentials=credentials, heartbeat=1000)
      connection = pika.BlockingConnection(connection_params)
      
      channel = connection.channel()
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
    credentials = pika.PlainCredentials(username=self.username, password=self.password)
    connection_params = pika.ConnectionParameters(host=self.host, port=self.port, credentials=credentials, heartbeat=1000)
    connection = pika.BlockingConnection(connection_params)
    
    message_body = json.dumps(data)
    channel = connection.channel()
    
    channel.exchange_declare(exchange=exchange, exchange_type='direct')
    channel.basic_publish(exchange=exchange, routing_key=route, body=message_body)
    connection.close()