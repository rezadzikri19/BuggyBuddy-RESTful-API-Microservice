from src.core.usecases.report_crud_usecase import ReportCRUDUsecase
from src.core.usecases.report_vectorize_usecase import ReportVectorizeUsecase

from src.infrastructure.main_drivers.report_crud_operator_driver import ReportCRUDOperatorDriver
from src.infrastructure.main_drivers.report_preprocessor_driver import ReportPreprocessorDriver
from src.infrastructure.main_drivers.revectorizer_driver import RevectorizerDriver

from src.infrastructure.logger.logger_driver import LoggerDriver

from infrastructure.api.routes import ApiRoutes

def main():
  logger_driver = LoggerDriver()
  
  report_crud_operator_driver = ReportCRUDOperatorDriver()

