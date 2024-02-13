from typing import Dict, Any

import re
import uuid

from pinecone import QueryResponse

from ...core.entities.report_entity import VectorizedReportEntity


def pinecone_response_to_report(response: QueryResponse) -> VectorizedReportEntity:
  return VectorizedReportEntity(
    id=response['metadata']['id'],
    component=response['metadata']['component'],
    description=response['metadata']['description'],
    platform=response['metadata']['platform'],
    product=response['metadata']['product'],
    summary=response['metadata']['summary'],
    type=response['metadata']['type'],
    vector=list(response['values'])
  )
  

def report_to_pinecone_vector(report: VectorizedReportEntity) -> Dict[str, Any]:
  report_id = str(uuid.uuid4()) if 'id' not in report else report['id']
  return {
      'id': report_id,
      'values': report['vector'],
      'metadata': {
        'id': report_id,
        'summary': report['summary'],
        'description': report['description'],
        'platform': report['platform'],
        'product': report['product'],
        'component': report['component'],
        'type': report['type']
      }
    }
  
  
def remove_non_null_values(obj: object):
  result = {key: value for key, value in obj.items() if value is not None}
  return result