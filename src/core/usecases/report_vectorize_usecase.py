from typing import List

from ...core.entities.report_entity import RawReportEntity

from ...core.ports.report_preprocessor_port import ReportPreprocessorPort
from ...core.ports.vectorizer_port import VectorizerPort
from ...core.ports.logger_port import LoggerPort

class ReportVectorizeUsecase:
  def __init__(
      self,
      report_preprocessor: ReportPreprocessorPort,
      vectorizer: VectorizerPort,
      logger: LoggerPort) -> None:
    self.report_preprocessor = report_preprocessor
    self.vectorizer = vectorizer
    self.logger = logger
    
  
  def report_vectorize(self, report: RawReportEntity) -> List[float]:
    try:
      features_to_drop = ['id', 'status', 'priority', 'resolution', 'severity', 'component', 'product', 'type']
      
      result = self.report_preprocessor.drop_features(report, features_to_drop)
      result = self.report_preprocessor.aggregate_text_features(result)
      result = self.report_preprocessor.clean_sentence(result)
      result = self.report_preprocessor.remove_stopwords(result)
      result = self.report_preprocessor.generate_sent_embedding(result)
      
      result = self.vectorizer.vectorize(result)
      return result
    except Exception as error:
      error_message = f'ReportVectorizeUsecase.report_vectorize: {error}'
      self.logger.log_error(error_message, error)