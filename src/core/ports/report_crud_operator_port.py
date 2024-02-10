from abc import ABC, abstractmethod
from typing import List

from ...core.entities.report_entity import VectorizedReportEntity
from ...core.dtos.report_crud_dto import GetReportQueryDTO

class ReportCRUDOperatorPort(ABC):
  @abstractmethod
  def create_report(self, report: VectorizedReportEntity) -> VectorizedReportEntity:
    pass
  
  @abstractmethod
  def get_reports(self, query: GetReportQueryDTO) -> List[VectorizedReportEntity]:
    pass
  
  @abstractmethod
  def get_similar_reports(self, report: VectorizedReportEntity) -> List[VectorizedReportEntity]:
    pass
  
  @abstractmethod
  def update_report(self, query: GetReportQueryDTO, report: VectorizedReportEntity) -> VectorizedReportEntity:
    pass
  
  @abstractmethod
  def delete_report(self, query: GetReportQueryDTO) -> None:
    pass