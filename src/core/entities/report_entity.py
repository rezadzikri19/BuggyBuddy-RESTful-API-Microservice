from typing import List, TypedDict, Optional

class RawReportEntity(TypedDict):
  id: Optional[int] = None
  summary: str
  description: str
  platform: str
  product: str
  component: str
  type: str
    
    
class VectorizedReportEntity(TypedDict):
  id: Optional[int] = None
  summary: str
  description: str
  platform: str
  product: str
  component: str
  type: str
  vector: List[float]
  