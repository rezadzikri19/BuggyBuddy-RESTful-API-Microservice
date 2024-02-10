from abc import ABC, abstractmethod
from typing import List

from ...core.entities.bug_report_entity import RawBugReportEntity
from ...core.dtos.report_preprocess_dto import DropFeaturesDTO, AggregateTextDTO, CleanSentenceDTO, RemoveStopwordsDTO, GenerateSentEmbeddingDTO

class ReportPreprocessorPort(ABC):
  @abstractmethod
  def drop_features(self, data: RawBugReportEntity, features_to_drop: List[str]) -> DropFeaturesDTO:
    pass
  
  @abstractmethod
  def aggregate_text_features(self, data) -> AggregateTextDTO:
    pass
  
  @abstractmethod
  def clean_sentence(self, data) -> CleanSentenceDTO:
    pass
  
  @abstractmethod
  def remove_stopwords(self, data) -> RemoveStopwordsDTO:
    pass
  
  @abstractmethod
  def generate_sent_embedding(self, data) -> GenerateSentEmbeddingDTO:
    pass