from typing import List
from io import BytesIO

import boto3
from keras.models import Model, load_model

from ...core.ports.revectorizer_port import RevectorizerPort
from ...core.ports.logger_port import LoggerPort

class S3RevectorizerDriver(RevectorizerPort):
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
      region_name=region_name
    )
    self.s3_client = session.client('s3')
    self.bucket_name = bucket_name
    self.logger = logger

  
  def revectorize(self, vector: List[float]) -> List[float]:
    try:
      file_name = '/TRAIN/models/embedding/model_embedding.bin'

      response = self.s3_client.get_object(Bucket=self.bucket_name, Key=file_name)
      model_data = response['Body'].read()
          
      revectorizer_model: Model = load_model(BytesIO(model_data))
      revector = revectorizer_model.predict([vector])
      return revector[0].tolist()
    except Exception as error:
      error_message = f'S3RevectorizerDriver.revectorize: {error}'
      self.logger.log_error(error_message, error)