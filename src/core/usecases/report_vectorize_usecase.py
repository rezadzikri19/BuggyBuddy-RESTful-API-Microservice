from ..entities.bug_report_entity import RawBugReportEntity

class ReportVectorizingUsecase:
  def __init__(self) -> None:
    pass
  
  def report_vectorize(self, report: RawBugReportEntity):
    result = self.report_preprocessor.drop_features(report)
    result = self.report_preprocessor.aggregate_text_features(result)
    result = self.report_preprocessor.clean_sentence(result)
    result = self.report_preprocessor.remove_stopwords(result)
    result = self.report_preprocessor.generate_sent_embedding(result)
    
    result = self.report_vectorizer.report_vectorize(result)
    return result