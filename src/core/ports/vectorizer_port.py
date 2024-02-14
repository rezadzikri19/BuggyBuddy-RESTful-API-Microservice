from abc import ABC, abstractmethod
from typing import List

class VectorizerPort(ABC):
  @abstractmethod
  def vectorize(self, vector: List[float]) -> List[float]:
    pass