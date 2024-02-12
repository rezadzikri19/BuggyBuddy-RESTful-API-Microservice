from typing import Dict, Any

import re
import nltk
import uuid

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from pinecone import QueryResponse

from ...core.entities.report_entity import VectorizedReportEntity

nltk.download('stopwords', quiet=True)
nltk.download('punkt', quiet=True)

def remove_special_chars(text: str):
  text = text.lower()
  text = re.sub(r'\n|\t|\r|\0', ' ', text)
  text = re.sub(r'[^a-zA-Z0-9\s]', ' ', text)
  text = re.sub(r'\s{2,}', ' ', text)
  text = re.sub(r'\s$', '', text)
  text = re.sub(r'\s[b-z]\s', ' ', text)
  text = re.sub(r'\s[b-z]\s', ' ', text)
  text = re.sub(r'\s{2,}', ' ', text)
  return text


def remove_stops(text: str):
  stop_words = set(stopwords.words('english'))
  words = word_tokenize(text)
  filtered_words = [word for word in words if word not in stop_words]
  return ' '.join(filtered_words)


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