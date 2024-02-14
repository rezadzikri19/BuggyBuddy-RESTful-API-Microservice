import os
from typing import List

import boto3
from keras.models import Model, load_model

from ...core.ports.vectorizer_port import VectorizerPort
from ...core.ports.logger_port import LoggerPort

class S3VectorizerDriver(VectorizerPort):
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

  
  def vectorize(self, vector: List[float]) -> List[float]:
    try:
      file_name = 'model_embedding.h5'
      s3_model_path = f'TRAIN/models/embedding/{file_name}'
      
      curr_dir = os.getcwd()
      data_dir = os.path.join(curr_dir, 'artifacts', 'models')
      
      if not os.path.exists(data_dir):
          os.makedirs(data_dir)
        
      model_path = os.path.join(data_dir, file_name)
      
      if not os.path.exists(model_path):
        self.s3_client.download_file(self.bucket_name, s3_model_path, model_path)
      
      vectorizer_model: Model = load_model(model_path)
      revector = vectorizer_model.predict([vector])
      
      return revector[0].tolist()
    except Exception as error:
      error_message = f'S3VectorizerDriver.vectorize: {error}'
      self.logger.log_error(error_message, error)