from abc import ABC, abstractmethod
from typing import List, Optional

from ...core.entities.report_entity import VectorizedReportEntity
from ...core.dtos.report_crud_dto import GetReportQueryDTO, UpdateReportDTO

class ReportCRUDOperatorPort(ABC):
  @abstractmethod
  def create_report(self, report: VectorizedReportEntity) -> VectorizedReportEntity:
    pass
  
  @abstractmethod
  def get_reports(self, query: GetReportQueryDTO) -> List[VectorizedReportEntity]:
    pass
  
  @abstractmethod
  def get_similar_reports(self, report: VectorizedReportEntity, threshold: Optional[float] = 0.5) -> List[VectorizedReportEntity]:
    pass
  
  @abstractmethod
  def update_report(self, report_id: str, report: VectorizedReportEntity) -> VectorizedReportEntity:
    pass
  
  @abstractmethod
  def delete_report(self, report_id: str) -> None:
    pass