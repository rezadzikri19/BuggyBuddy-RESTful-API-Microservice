from typing import TypedDict, Optional

class ReportDTO(TypedDict):
  summary: str
  description: str
  platform: str
  product: str
  component: str
  type: str

class GetReportQueryDTO(TypedDict):
  id: Optional[int]
  platform: Optional[str]
  product: Optional[str]
  component: Optional[str]
  type: Optional[str]


class UpdateReportDTO(TypedDict):
  summary: Optional[str]
  description: Optional[str]
  platform: Optional[str]
  product: Optional[str]
  component: Optional[str]
  type: Optional[str]