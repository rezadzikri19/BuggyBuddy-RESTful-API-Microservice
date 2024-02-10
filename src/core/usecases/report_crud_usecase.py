from ..entities.bug_report_entity import RawBugReportEntity

class BugReportUsecase:
  def __init__(self) -> None:
    pass
  
  def get_similar_reports(self, report: RawBugReportEntity):
    result = self.report_vectorize_usecase.report_vectorize(report)
    result = self.report_vectorize_usecase.similar_reports(result)
    return result
  
  def create_new_report(self):
    pass