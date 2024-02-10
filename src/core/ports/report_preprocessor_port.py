from abc import ABC, abstractmethod
from typing import List

from ..entities.bug_report_entity import RawBugReportEntity

class DataPreprocessorPort(ABC):
  @abstractmethod
  def drop_features(self, data: RawBugReportEntity, features_to_drop: List[str]):
    pass
  
  @abstractmethod
  def aggregate_text_features(self, data):
    pass
  
  @abstractmethod
  def clean_sentence(self, data):
    pass
  
  @abstractmethod
  def remove_stopwords(self, data):
    pass
  
  @abstractmethod
  def generate_sent_embedding(self, data):
    pass