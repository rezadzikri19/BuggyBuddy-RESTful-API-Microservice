from typing import List

from ...core.usecases.report_crud_usecase import ReportCRUDUsecase
from ...infrastructure.api.api_dtos import *

from fastapi import APIRouter

router = APIRouter()

class ApiRoutes():
  def __init__(self, report_crud_usecase: ReportCRUDUsecase) -> None:
    self.report_crud_usecase = report_crud_usecase
  
  @router.post('/report')
  async def create_report(self, report: RequestReportDTO) -> ResponseGetReportDTO:
    result = self.report_crud_usecase.create_new_report(report)
    return result
  
  @router.get('/reports')
  async def get_reports(self, query: RequestGetReportQueryDTO) -> List[ResponseGetReportDTO]:
    result = self.report_crud_usecase.get_reports(query)
    return result
  
  @router.get('/reports/similar')
  async def get_reports(self, report: RequestReportDTO) -> List[ResponseGetReportDTO]:
    result = self.report_crud_usecase.get_similar_reports(report)
    return result
  
  @router.put('/reports/{report_id}')
  async def update_report(self, report_id: str, report: RequestUpdateReportDTO) -> ResponseGetReportDTO:
    result = self.report_crud_usecase.update_report({ 'id': report_id }, report)
    return result
  
  @router.delete('/reports/{report_id}')
  async def update_report(self, report_id: str) -> ResponseGetReportDTO:
    result = self.report_crud_usecase.delete_report({ 'id': report_id })
    return result