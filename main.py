import os
from dotenv import load_dotenv
from pinecone import Pinecone
from fastapi import FastAPI, APIRouter

from src.core.usecases.report_crud_usecase import ReportCRUDUsecase
from src.core.usecases.report_vectorize_usecase import ReportVectorizeUsecase

from src.infrastructure.main_drivers.report_crud_operator_driver import ReportCRUDOperatorDriver
from src.infrastructure.main_drivers.report_preprocessor_driver import ReportPreprocessorDriver
from src.infrastructure.main_drivers.local_vectorizer_driver import LocalVectorizerDriver
from src.infrastructure.main_drivers.s3_vectorizer_driver import S3VectorizerDriver

from src.infrastructure.logger.logger_driver import LoggerDriver

from src.infrastructure.api.routes import api_routers

load_dotenv()

AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
REGION_NAME = os.getenv('REGION_NAME')
BUCKET_NAME = os.getenv('BUCKET_NAME')
PINECONE_API_KEY = os.getenv('PINECONE_API_KEY')
PINECONE_INDEX = os.getenv('PINECONE_INDEX')

pc_index = Pinecone(api_key=PINECONE_API_KEY).Index(PINECONE_INDEX)
logger_driver = LoggerDriver()

def crud_usecase_builder():
  try:
    report_preprocessor_driver = ReportPreprocessorDriver(logger_driver)
    # vectorizer_driver = LocalVectorizerDriver(logger_driver)
    vectorizer_driver = S3VectorizerDriver(
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
        region_name=REGION_NAME,
        bucket_name=BUCKET_NAME,
        logger=logger_driver
      )
    report_crud_operator_driver = ReportCRUDOperatorDriver(pc_index, logger_driver)
    
    report_vectorize_usecase = ReportVectorizeUsecase(
      report_preprocessor=report_preprocessor_driver,
      vectorizer=vectorizer_driver,
      logger=logger_driver)
    report_crud_usecase = ReportCRUDUsecase(
      report_crud_operator=report_crud_operator_driver,
      report_vectorize_usecase=report_vectorize_usecase,
      logger=logger_driver)
    
    return report_crud_usecase
  except Exception as error:
    error_message = f'main:crud_usecase_builder: {error}'
    logger_driver.log_error(error_message, error)


app = FastAPI(swagger_ui_parameters={'syntaxHighlight.theme': 'obsidian'})
router = APIRouter(prefix='/api')

report_crud_usecase = crud_usecase_builder()
api_routes = api_routers(router, report_crud_usecase)

app.include_router(api_routes)
  

