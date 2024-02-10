from typing import List

from ...core.entities.report_entity import RawReportEntity

from ...core.ports.report_preprocessor_port import ReportPreprocessorPort
from ...core.ports.revectorizer_port import RevectorizerPort

class ReportVectorizeUsecase:
  def __init__(
      self,
      report_preprocessor: ReportPreprocessorPort,
      revectorizer: RevectorizerPort) -> None:
    self.report_preprocessor = report_preprocessor
    self.revectorizer = revectorizer
    
  
  def report_vectorize(self, report: RawReportEntity) -> List[float]:
    result = self.report_preprocessor.drop_features(report)
    result = self.report_preprocessor.aggregate_text_features(result)
    result = self.report_preprocessor.clean_sentence(result)
    result = self.report_preprocessor.remove_stopwords(result)
    result = self.report_preprocessor.generate_sent_embedding(result)
    
    result = self.revectorizer.revectorize(result)
    return result