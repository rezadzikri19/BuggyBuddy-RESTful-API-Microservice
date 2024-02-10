from abc import ABC, abstractmethod
from typing import List

from ...core.entities.report_entity import RawReportEntity
from ...core.dtos.report_preprocess_dto import DropFeaturesDTO

class ReportPreprocessorPort(ABC):
  @abstractmethod
  def drop_features(self, data: RawReportEntity, features_to_drop: List[str]) -> DropFeaturesDTO:
    pass
  
  @abstractmethod
  def aggregate_text_features(self, data: DropFeaturesDTO) -> str:
    pass
  
  @abstractmethod
  def clean_sentence(self, text: str) -> str:
    pass
  
  @abstractmethod
  def remove_stopwords(self, text: str) -> str:
    pass
  
  @abstractmethod
  def generate_sent_embedding(self, text: str) -> List[float]:
    pass