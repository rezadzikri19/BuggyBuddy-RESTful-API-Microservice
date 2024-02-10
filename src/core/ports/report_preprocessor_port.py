from abc import ABC, abstractmethod
from typing import List

from ...core.entities.report_entity import RawReportEntity
from ...core.dtos.report_preprocess_dto import DropFeaturesDTO, AggregateTextDTO, CleanSentenceDTO, RemoveStopwordsDTO, GenerateSentEmbeddingDTO

class ReportPreprocessorPort(ABC):
  @abstractmethod
  def drop_features(self, data: RawReportEntity, features_to_drop: List[str]) -> DropFeaturesDTO:
    pass
  
  @abstractmethod
  def aggregate_text_features(self, data: DropFeaturesDTO) -> AggregateTextDTO:
    pass
  
  @abstractmethod
  def clean_sentence(self, data: AggregateTextDTO) -> CleanSentenceDTO:
    pass
  
  @abstractmethod
  def remove_stopwords(self, data: CleanSentenceDTO) -> RemoveStopwordsDTO:
    pass
  
  @abstractmethod
  def generate_sent_embedding(self, data: RemoveStopwordsDTO) -> GenerateSentEmbeddingDTO:
    pass