from typing import List, TypedDict, NotRequired

class GetReportQueryDTO(TypedDict):
  id: NotRequired[int]
  platform: NotRequired[str]
  product: NotRequired[str]
  component: NotRequired[str]
  type: NotRequired[str]


class UpdateReportDTO(TypedDict):
  id: NotRequired[int]
  summary: NotRequired[str]
  description: NotRequired[str]
  platform: NotRequired[str]
  product: NotRequired[str]
  component: NotRequired[str]
  type: NotRequired[str]