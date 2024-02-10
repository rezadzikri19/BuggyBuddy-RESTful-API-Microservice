from typing import List, TypedDict, NotRequired

class GetReportQueryDTO(TypedDict):
  id: NotRequired[int]
  platform: NotRequired[str]
  product: NotRequired[str]
  component: NotRequired[str]
  type: NotRequired[str]


class CreateReportDTO(TypedDict):
  id: int
  summary: str
  description: str
  platform: str
  product: str
  component: str
  type: str


class UpdateReportDTO(TypedDict):
  id: NotRequired[int]
  summary: NotRequired[str]
  description: NotRequired[str]
  platform: NotRequired[str]
  product: NotRequired[str]
  component: NotRequired[str]
  type: NotRequired[str]