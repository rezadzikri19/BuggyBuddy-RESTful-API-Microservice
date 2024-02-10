from ...core.entities.report_entity import RawReportEntity

from ...core.dtos.report_crud_dto import GetReportQueryDTO, UpdateReportDTO

from ...core.ports.report_crud_operator_port import ReportCRUDOperatorPort
from ...core.usecases.report_vectorize_usecase import ReportVectorizeUsecase

class BugReportUsecase:
  def __init__(
      self,
      report_crud_operator: ReportCRUDOperatorPort,
      report_vectorize_usecase: ReportVectorizeUsecase) -> None:
    self.report_crud_operator = report_crud_operator
    self.report_vectorize_usecase = report_vectorize_usecase
  
  
  def get_reports(self, query: GetReportQueryDTO) -> RawReportEntity:
    result = self.report_crud_operator.get_reports(query)
    return result
  
  
  def get_similar_reports(self, report: RawReportEntity):
    vector = self.report_vectorize_usecase.report_vectorize(report)
    vectorized_report = {**report, vector: vector}
    
    result = self.report_crud_operator.get_similar_reports(vectorized_report)
    result = result if result else []
    return result
  
  
  def create_new_report(self, report: RawReportEntity):
    vector = self.report_vectorize_usecase.report_vectorize(report)
    vectorized_report = {**report, vector: vector}
    
    result = self.report_crud_operator.create_report(vectorized_report)
    return result
  

  def update_report(self, query: GetReportQueryDTO, report: UpdateReportDTO):
    exist_report = self.report_crud_operator.get_reports(query)
    
    if not exist_report:
      raise Exception('report not found!')
    
    vector = self.report_vectorize_usecase.report_vectorize(exist_report[0])
    vectorized_report = {**exist_report[0], **report, vector: vector}
    
    result = self.report_crud_operator.update_report(query, vectorized_report)
    return result
  
  
  def delete_report(self, query: GetReportQueryDTO):
    exist_report = self.report_crud_operator.get_reports(query)
    
    if not exist_report:
      raise Exception('report not found!')
    
    self.report_crud_operator.delete_report(query)
    return exist_report