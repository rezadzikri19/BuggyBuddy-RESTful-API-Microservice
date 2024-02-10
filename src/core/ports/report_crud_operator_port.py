from abc import ABC, abstractmethod
from typing import List, Pa

from ...core.entities.bug_report_entity import VectorizedBugReportEntity

class ReportCRUDOperatorPort(ABC):
  @abstractmethod
  def create_report(self, report: VectorizedBugReportEntity) -> VectorizedBugReportEntity:
    pass
  
  @abstractmethod
  def get_reports(self, query) -> List[VectorizedBugReportEntity]:
    pass
  
  @abstractmethod
  def get_similar_reports(self, report: VectorizedBugReportEntity) -> List[VectorizedBugReportEntity]:
    pass
  
  @abstractmethod
  def update_report(self, query, report) -> VectorizedBugReportEntity:
    pass