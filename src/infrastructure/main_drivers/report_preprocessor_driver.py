from typing import List

import re
import nltk

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from sentence_transformers import SentenceTransformer

from ...core.dtos.report_preprocess_dto import AggregateTextDTO

from ...core.dtos.report_preprocess_dto import DropFeaturesDTO
from ...core.entities.report_entity import RawReportEntity
from ...core.ports.report_preprocessor_port import ReportPreprocessorPort

from ...infrastructure.utils.common_util import remove_special_chars, remove_stops

nltk.download('stopwords')
nltk.download('punkt')

class ReportPreprocessorDriver(ReportPreprocessorPort):
  def __init__(self) -> None:
    pass
  
  
  def drop_features(self, data: RawReportEntity, features_to_drop: List[str]) -> DropFeaturesDTO:
    result = {key: value for key, value in data.items() if key not in features_to_drop}
    return result
    
    
  def aggregate_text_features(self, data: DropFeaturesDTO) -> str:
    text = data['platform'] + data['summary'] + data['description']
    result = {'text': text}
    return result
  
  
  def clean_sentence(self, text: str) -> str:
    result = text.lower()
    result = re.sub(r'\n|\t|\r|\0', ' ', result)
    result = re.sub(r'[^a-zA-Z0-9\s]', ' ', result)
    result = re.sub(r'\s{2,}', ' ', result)
    result = re.sub(r'\s$', '', result)
    result = re.sub(r'\s[b-z]\s', ' ', result)
    result = re.sub(r'\s[b-z]\s', ' ', result)
    result = re.sub(r'\s{2,}', ' ', result)
    return result
  
  
  def remove_stopwords(self, text: str) -> str:
    stop_words = set(stopwords.words('english'))
    words = word_tokenize(text)
    
    filtered_words = [word for word in words if word not in stop_words]
    result = ' '.join(filtered_words)
    return result
  
  
  def generate_sent_embedding(self, text: str) -> List[float]:
    sent_embd_model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
    result = sent_embd_model.encode(text).tolist()
    return result
    