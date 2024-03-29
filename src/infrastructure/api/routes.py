from typing import List

from ...core.usecases.report_crud_usecase import ReportCRUDUsecase
from ...infrastructure.api.api_dtos import RequestReportDTO, ResponseGetReportDTO, RequestGetReportQueryDTO, RequestUpdateReportDTO

from fastapi import APIRouter, HTTPException

def api_routers(router: APIRouter, report_crud_usecase: ReportCRUDUsecase) -> APIRouter:
  @router.post('/reports/')
  async def create_report(report: RequestReportDTO) -> ResponseGetReportDTO:
    report = report.model_dump(exclude_none=True)
    result = report_crud_usecase.create_new_report(report)
    return result
  
  @router.get('/reports/')
  async def get_reports(query: RequestGetReportQueryDTO) -> List[ResponseGetReportDTO]:
    query = query.model_dump(exclude_none=True)
    result = report_crud_usecase.get_reports(query)
    return result
  
  @router.get('/reports/similar/')
  async def get_reports(report: RequestReportDTO) -> List[ResponseGetReportDTO]:
    report = report.model_dump(exclude_none=True)
    result = report_crud_usecase.get_similar_reports(report)
    return result
  
  @router.put('/reports/{report_id}/')
  async def update_report(report_id: str, report: RequestUpdateReportDTO) -> ResponseGetReportDTO:
    report = report.model_dump(exclude_none=True)
    result = report_crud_usecase.update_report({ 'id': report_id }, report)
    return result
  
  @router.delete('/reports/{report_id}/')
  async def update_report(report_id: str) -> ResponseGetReportDTO:
    try:
      result = report_crud_usecase.delete_report({ 'id': report_id })
      return result
    except Exception as error:
      raise HTTPException(status_code=500, detail=error)

  return router
  
