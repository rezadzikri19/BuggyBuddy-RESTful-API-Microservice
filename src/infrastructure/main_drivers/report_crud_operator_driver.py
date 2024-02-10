from typing import List, Optional

from ...core.dtos.report_crud_dto import GetReportQueryDTO
from ...core.entities.report_entity import VectorizedReportEntity
from ...core.ports.report_crud_operator_port import ReportCRUDOperatorPort

from ...infrastructure.utils.common_util import report_to_pinecone_vector, pinecone_response_to_report

from pinecone import Index

class ReportCRUDOperatorDriver(ReportCRUDOperatorPort):
  def __init__(self, pinecone_index: Index) -> None:
    self.pinecone_index = pinecone_index
    
    
  def create_report(self, report: VectorizedReportEntity) -> VectorizedReportEntity:
    inserted_vectors = [report_to_pinecone_vector(report)]
    self.pinecone_index.upsert(vectors=inserted_vectors)
    return report
  
  
  def get_reports(self, query: GetReportQueryDTO) -> List[VectorizedReportEntity]:
    response = self.pinecone_index.query(
        vector=[0 for _ in range(128)],
        filter=query,
        top_k=5,
        include_metadata=True,
        include_values=True
      )
    
    result = [pinecone_response_to_report(item) for item in response['matches']]
    return result
  
  
  def get_similar_reports(self, report: VectorizedReportEntity, threshold: Optional[float] = 0.5) -> List[VectorizedReportEntity]:
    response = self.pinecone_index.query(
        vector=report['vector'],
        top_k=5,
        include_metadata=True,
        include_values=True
      )
    
    result = [pinecone_response_to_report(item) for item in response['matches'] if item['score'] >= threshold]
    return result
  
  
  def update_report(self, report_id: str, report: VectorizedReportEntity) -> VectorizedReportEntity:
    pinecone_vector = report_to_pinecone_vector(report)
    self.pinecone_index.update(
        id=report_id,
        values=report['vector'],
        set_metadata=pinecone_vector['metadata'],
      )
    return report
  
  
  def delete_report(self, report_id: str) -> None:
    self.pinecone_index.delete(ids=[report_id])
  