from typing import List, Optional

from ...core.dtos.report_crud_dto import GetReportQueryDTO
from ...core.entities.report_entity import VectorizedReportEntity

from ...core.ports.report_crud_operator_port import ReportCRUDOperatorPort
from ...core.ports.logger_port import LoggerPort

from ...infrastructure.utils.common_util import report_to_pinecone_vector, pinecone_response_to_report, remove_non_null_values

from pinecone import Index

class ReportCRUDOperatorDriver(ReportCRUDOperatorPort):
  def __init__(
      self,
      pinecone_index: Index,
      logger: LoggerPort) -> None:
    self.pinecone_index = pinecone_index
    self.logger = logger
    
    
  def create_report(self, report: VectorizedReportEntity) -> VectorizedReportEntity:
    try:
      pinecone_vector = report_to_pinecone_vector(report)
      self.pinecone_index.upsert(vectors=[pinecone_vector])
      return pinecone_vector['metadata']
    except Exception as error:
      error_message = f'ReportCRUDOperatorDriver.create_report: {error}'
      self.logger.log_error(error_message, error)
  
  
  def get_reports(self, query: GetReportQueryDTO) -> List[VectorizedReportEntity]:
    try:
      query = remove_non_null_values(query)
      response = self.pinecone_index.query(
          vector=[0 for _ in range(128)],
          filter=query,
          top_k=5,
          include_metadata=True,
          include_values=True
        )
      result = [pinecone_response_to_report(item) for item in response['matches']]
      return result
    except Exception as error:
      error_message = f'ReportCRUDOperatorDriver.get_reports: {error}'
      self.logger.log_error(error_message, error)
  
  
  def get_similar_reports(self, report: VectorizedReportEntity, threshold: Optional[float] = 0.5) -> List[VectorizedReportEntity]:
    try:
      response = self.pinecone_index.query(
          vector=report['vector'],
          top_k=5,
          include_metadata=True,
          include_values=True
        )
      result = [pinecone_response_to_report(item) for item in response['matches'] if item['score'] >= threshold]
      return result
    except Exception as error:
      error_message = f'ReportCRUDOperatorDriver.get_similar_reports: {error}'
      self.logger.log_error(error_message, error)
  
  
  def update_report(self, report_id: str, report: VectorizedReportEntity) -> VectorizedReportEntity:
    try:
      pinecone_vector = report_to_pinecone_vector(report)
      self.pinecone_index.update(
          id=report_id,
          values=report['vector'],
          set_metadata=pinecone_vector['metadata'],
        )
      return pinecone_vector['metadata']
    except Exception as error:
      error_message = f'ReportCRUDOperatorDriver.update_report: {error}'
      self.logger.log_error(error_message, error)
  
  
  def delete_report(self, report_id: str) -> None:
    try:
      self.pinecone_index.delete(ids=[report_id])
    except Exception as error:
      error_message = f'ReportCRUDOperatorDriver.delete_report: {error}'
      self.logger.log_error(error_message, error)
  