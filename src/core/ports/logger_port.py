from abc import ABC, abstractmethod
from typing import Optional

class LoggerPort(ABC):
  @abstractmethod
  def log_info(self, message: str = 'None') -> None:
    pass
  
  @abstractmethod
  def log_error(self, message: str = 'None', error: Optional[Exception] = None) -> None:
    pass