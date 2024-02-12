from typing import TypedDict, Optional

class ReportDTO(TypedDict):
  summary: str
  description: str
  platform: str
  product: str
  component: str
  type: str

class GetReportQueryDTO(TypedDict):
  id: Optional[str] = None
  summary: Optional[str] = None
  description: Optional[str] = None
  platform: Optional[str] = None
  product: Optional[str] = None
  component: Optional[str] = None
  type: Optional[str] = None


class UpdateReportDTO(TypedDict):
  summary: Optional[str]  = None
  description: Optional[str]  = None
  platform: Optional[str]  = None
  product: Optional[str]  = None
  component: Optional[str]  = None
  type: Optional[str]  = None