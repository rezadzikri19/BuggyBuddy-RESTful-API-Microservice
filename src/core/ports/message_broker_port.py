from typing import Callable, Dict, Any
from abc import ABC, abstractmethod

class MessageBrokerPort(ABC):
  @abstractmethod
  def publish_message(self, exchange: str, route: str, data: Dict[str, Any]) -> None:
    pass
  
  @abstractmethod
  def subscribe_topic(self, exchange: str, route: str, callback: Callable[[Dict[str, Any]], None]) -> None:
    pass