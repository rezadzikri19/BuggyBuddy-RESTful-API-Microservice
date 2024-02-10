from typing import List, TypedDict

class RawBugReportEntity(TypedDict):
  id: int
  summary: str
  description: str
  platform: str
  product: str
  component: str
  type: str
    
    
class VectorizedBugReportEntity(TypedDict):
  id: int
  summary: str
  description: str
  platform: str
  product: str
  component: str
  type: str
  vector: List[float]
  