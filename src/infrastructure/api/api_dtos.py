from typing import Optional, List
from pydantic import BaseModel

class RequestReportDTO(BaseModel):
  summary: str
  description: str
  platform: str
  product: str
  component: str
  type: str


class RequestGetReportQueryDTO(BaseModel):
  id: Optional[str] = None
  summary: Optional[str] = None
  description: Optional[str] = None
  platform: Optional[str] = None
  product: Optional[str] = None
  component: Optional[str] = None
  type: Optional[str] = None


class RequestUpdateReportDTO(BaseModel):
  id: Optional[str] = None
  summary: Optional[str] = None
  description: Optional[str] = None
  platform: Optional[str] = None
  product: Optional[str] = None
  component: Optional[str] = None
  type: Optional[str] = None
  

class ResponseGetReportDTO(BaseModel):
  id: str
  summary: str
  description: str
  platform: str
  product: str
  component: str
  type: str
  vector: Optional[List[float]] = None