from typing import List, TypedDict

class RawReportEntity(TypedDict):
  id: int
  summary: str
  description: str
  platform: str
  product: str
  component: str
  type: str
    
    
class VectorizedReportEntity(TypedDict):
  id: int
  summary: str
  description: str
  platform: str
  product: str
  component: str
  type: str
  vector: List[float]
  