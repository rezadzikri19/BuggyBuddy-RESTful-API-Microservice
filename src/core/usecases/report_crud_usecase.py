from typing import List

from ...core.entities.report_entity import VectorizedReportEntity

from ...core.dtos.report_crud_dto import GetReportQueryDTO, UpdateReportDTO, ReportDTO

from ...core.ports.report_crud_operator_port import ReportCRUDOperatorPort
from ...core.usecases.report_vectorize_usecase import ReportVectorizeUsecase

class ReportCRUDUsecase:
  def __init__(
      self,
      report_crud_operator: ReportCRUDOperatorPort,
      report_vectorize_usecase: ReportVectorizeUsecase) -> None:
    self.report_crud_operator = report_crud_operator
    self.report_vectorize_usecase = report_vectorize_usecase
  
  
  def get_reports(self, query: GetReportQueryDTO) -> VectorizedReportEntity:
    result = self.report_crud_operator.get_reports(query)
    return result
  
  
  def get_similar_reports(self, report: ReportDTO) -> List[VectorizedReportEntity]:
    vector = self.report_vectorize_usecase.report_vectorize(report)
    vectorized_report = {**report, vector: vector}
    
    result = self.report_crud_operator.get_similar_reports(vectorized_report)
    result = result if result else []
    return result
  
  
  def create_new_report(self, report: ReportDTO) -> VectorizedReportEntity:
    vector = self.report_vectorize_usecase.report_vectorize(report)
    vectorized_report = {**report, vector: vector}
    
    self.report_crud_operator.create_report(vectorized_report)
    return report
  

  def update_report(self, query: GetReportQueryDTO, report: UpdateReportDTO) -> VectorizedReportEntity:
    exist_report = self.report_crud_operator.get_reports(query)
    
    if not exist_report:
      raise Exception('report not found!')
    
    vector = self.report_vectorize_usecase.report_vectorize(exist_report[0])
    vectorized_report = {**exist_report[0], **report, vector: vector}
    
    self.report_crud_operator.update_report(query['id'], vectorized_report)
    return vectorized_report
  
  
  def delete_report(self, query: GetReportQueryDTO) -> VectorizedReportEntity:
    exist_report = self.report_crud_operator.get_reports(query)
    
    if not exist_report:
      raise Exception('report not found!')
    
    self.report_crud_operator.delete_report(query['id'])
    return exist_report