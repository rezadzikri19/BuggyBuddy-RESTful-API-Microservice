from typing import List

from ...core.entities.report_entity import VectorizedReportEntity
from ...core.dtos.report_crud_dto import GetReportQueryDTO, UpdateReportDTO, ReportDTO

from ...core.ports.report_crud_operator_port import ReportCRUDOperatorPort
from ...core.ports.logger_port import LoggerPort

from ...core.usecases.report_vectorize_usecase import ReportVectorizeUsecase

class ReportCRUDUsecase:
  def __init__(
      self,
      report_crud_operator: ReportCRUDOperatorPort,
      report_vectorize_usecase: ReportVectorizeUsecase,
      logger: LoggerPort) -> None:
    self.report_crud_operator = report_crud_operator
    self.report_vectorize_usecase = report_vectorize_usecase
    self.logger = logger
  
  
  def get_reports(self, query: GetReportQueryDTO) -> VectorizedReportEntity:
    try:
      result = self.report_crud_operator.get_reports(query)
      return result
    except Exception as error:
      error_message = f'ReportCRUDUsecase.get_reports: {error}'
      self.logger.log_error(error_message, error)
  
  
  def get_similar_reports(self, report: ReportDTO) -> List[VectorizedReportEntity]:
    try:
      vector = self.report_vectorize_usecase.report_vectorize(report)
      vectorized_report = {**report, 'vector': vector}
      
      result = self.report_crud_operator.get_similar_reports(vectorized_report)
      result = result if result else []
      return result
    except Exception as error:
      error_message = f'ReportCRUDUsecase.get_similar_reports: {error}'
      self.logger.log_error(error_message, error)
  
  def create_new_report(self, report: ReportDTO) -> VectorizedReportEntity:
    try:
      vector = self.report_vectorize_usecase.report_vectorize(report)
      vectorized_report = {**report, 'vector': vector}
      
      result = self.report_crud_operator.create_report(vectorized_report)
      return result
    except Exception as error:
      error_message = f'ReportCRUDUsecase.create_new_report: {error}'
      self.logger.log_error(error_message, error)
  

  def update_report(self, query: GetReportQueryDTO, report: UpdateReportDTO) -> VectorizedReportEntity:
    try:
      exist_report = self.report_crud_operator.get_reports(query)
      
      if not exist_report:
        raise Exception('report not found!')
      
      vector = self.report_vectorize_usecase.report_vectorize(exist_report[0])
      vectorized_report = {**exist_report[0], **report, 'vector': vector}
      
      self.report_crud_operator.update_report(query['id'], vectorized_report)
      return vectorized_report
    except Exception as error:
      error_message = f'ReportCRUDUsecase.update_report: {error}'
      self.logger.log_error(error_message, error)
  
  
  def delete_report(self, query: GetReportQueryDTO) -> VectorizedReportEntity:
    try:  
      exist_report = self.report_crud_operator.get_reports(query)
      
      if not exist_report:
        raise Exception('report not found!')
      
      self.report_crud_operator.delete_report(query['id'])
      return exist_report[0]
    except Exception as error:
      error_message = f'ReportCRUDUsecase.delete_report: {error}'
      self.logger.log_error(error_message, error)