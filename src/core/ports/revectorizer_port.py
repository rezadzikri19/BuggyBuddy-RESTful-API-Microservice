from abc import ABC, abstractmethod
from typing import List

class RevectorizerPort(ABC):
  @abstractmethod
  def revectorize(vector: List[float]) -> List[float]:
    pass