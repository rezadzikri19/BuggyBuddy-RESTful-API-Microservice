from src.core.usecases.report_crud_usecase import ReportCRUDUsecase
from src.core.usecases.report_vectorize_usecase import ReportVectorizeUsecase

from src.infrastructure.main_drivers.report_crud_operator_driver import ReportCRUDOperatorDriver
from src.infrastructure.main_drivers.report_preprocessor_driver import ReportPreprocessorDriver
from src.infrastructure.main_drivers.revectorizer_driver import RevectorizerDriver

from src.infrastructure.logger.logger_driver import LoggerDriver

from src.infrastructure.api.routes import ApiRoutes

from pinecone import Pinecone
from fastapi import FastAPI

def main():
  logger_driver = LoggerDriver()
  
  try:
    app = FastAPI()
    pc = Pinecone(api_key="d5532e31-0f59-48ce-a12a-743f75e16b5f")
    pc_index = pc.Index('bug-report-index')
    
    report_preprocessor_driver = ReportPreprocessorDriver(logger_driver)
    revectorizer_driver = RevectorizerDriver(logger_driver)
    report_crud_operator_driver = ReportCRUDOperatorDriver(logger_driver, pinecone_index=pc_index)
    
    report_vectorize_usecase = ReportVectorizeUsecase(
      report_preprocessor=report_preprocessor_driver,
      revectorizer=revectorizer_driver,
      logger=logger_driver)
    report_crud_usecase = ReportCRUDUsecase(
      report_crud_operator=report_crud_operator_driver,
      report_vectorize_usecase=report_vectorize_usecase,
      logger=logger_driver)
    
    api_routes = ApiRoutes(report_crud_usecase)
    app.include_router(api_routes)
  except Exception as error:
    error_message = f'main: {error}'
    logger_driver.log_error(error_message, error)

if __name__ == "__main__":
  main()
  

