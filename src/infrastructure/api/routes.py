from typing import List

from ...core.usecases.report_crud_usecase import ReportCRUDUsecase
from ...core.dtos.report_crud_dto import GetReportQueryDTO
from ...infrastructure.api.api_dtos import *

from fastapi import APIRouter

def api_routers(router: APIRouter, report_crud_usecase: ReportCRUDUsecase) -> APIRouter:
  @router.post('/reports')
  async def create_report(report: RequestReportDTO) -> ResponseGetReportDTO:
    report = report.model_dump(exclude_none=True)
    result = report_crud_usecase.create_new_report(report)
    return result
  
  @router.get('/reports')
  async def get_reports(
      id: Optional[str] = None,
      summary: Optional[str] = None,
      description: Optional[str] = None,
      platform: Optional[str] = None,
      product: Optional[str] = None,
      component: Optional[str] = None,
      type: Optional[str] = None) -> List[ResponseGetReportDTO]:
    query: GetReportQueryDTO = {
      'id': id,
      'component': component,
      'description': description,
      'platform': platform,
      'product': product,
      'summary': summary,
      'type': type
    }
    result = report_crud_usecase.get_reports(query)
    return result
  
  @router.get('/reports/similar')
  async def get_reports(report: RequestReportDTO) -> List[ResponseGetReportDTO]:
    report = report.model_dump(exclude_none=True)
    result = report_crud_usecase.get_similar_reports(report)
    return result
  
  @router.put('/reports/{report_id}')
  async def update_report(report_id: str, report: RequestUpdateReportDTO) -> ResponseGetReportDTO:
    report = report.model_dump(exclude_none=True)
    result = report_crud_usecase.update_report({ 'id': report_id }, report)
    return result
  
  @router.delete('/reports/{report_id}')
  async def update_report(report_id: str) -> ResponseGetReportDTO:
    result = report_crud_usecase.delete_report({ 'id': report_id })
    return result
  
  return router
  
