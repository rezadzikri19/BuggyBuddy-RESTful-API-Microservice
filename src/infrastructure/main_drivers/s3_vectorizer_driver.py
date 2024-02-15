import os
from typing import List

import boto3
from keras.models import load_model

from ...core.ports.vectorizer_port import VectorizerPort
from ...core.ports.logger_port import LoggerPort

class S3VectorizerDriver(VectorizerPort):
  _vectorizer_model = None
  
  def __init__(
      self,
      aws_access_key_id: str,
      aws_secret_access_key: str,
      region_name: str,
      bucket_name: str,
      logger: LoggerPort) -> None:
    session = boto3.Session(
      aws_access_key_id=aws_access_key_id,
      aws_secret_access_key=aws_secret_access_key,
      region_name=region_name)
    self.s3_client = session.client('s3')
    self.bucket_name = bucket_name
    self.logger = logger
    self.initiate_model()


  def initiate_model(self) -> None:
    try:
      file_name = 'model_embedding.h5'
      s3_model_path = f'TRAIN/models/embedding/{file_name}'
      
      data_dir = os.path.join(os.getcwd(), 'artifacts', 'models')
      os.makedirs(data_dir, exist_ok=True)
      model_path = os.path.join(data_dir, file_name)
      
      self.s3_client.download_file(self.bucket_name, s3_model_path, model_path)
      S3VectorizerDriver._vectorizer_model = load_model(model_path)
    except Exception as error:
      error_message = f'S3VectorizerDriver.initiate_model: {error}'
      self.logger.log_error(error_message, error)
  
  
  def vectorize(self, vector: List[float]) -> List[float]:
    try:
      if S3VectorizerDriver._vectorizer_model is None:
        raise Exception('vectorizer model not found!')
      
      vectorized = S3VectorizerDriver._vectorizer_model.predict([vector])
      return vectorized[0].tolist()
    except Exception as error:
      error_message = f'S3VectorizerDriver.vectorize: {error}'
      self.logger.log_error(error_message, error)