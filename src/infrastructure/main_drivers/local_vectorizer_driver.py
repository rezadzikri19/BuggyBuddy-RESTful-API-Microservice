import os
from typing import List

from keras.models import Model, load_model

from ...core.ports.vectorizer_port import VectorizerPort
from ...core.ports.logger_port import LoggerPort

class LocalVectorizerDriver(VectorizerPort):
  _vectorizer_model = None
  
  def __init__(self, logger: LoggerPort) -> None:
    self.logger = logger
    self.initiate_model()


  def initiate_model(self) -> None:
    try:
      data_dir = os.path.join(os.getcwd(), 'artifacts', 'models')
      os.makedirs(data_dir, exist_ok=True)
      
      file_name = 'model_embedding.h5'
      data_path = os.path.join(data_dir, file_name)
      LocalVectorizerDriver._vectorizer_model = load_model(data_path)
    except Exception as error:
      error_message = f'LocalVectorizerDriver.vectorize: {error}'
      self.logger.log_error(error_message, error)

  
  def vectorize(self, vector: List[float]) -> List[float]:
    try:
      if LocalVectorizerDriver._vectorizer_model is None:
        raise Exception('vectorizer model not found!')
      
      vectorized = LocalVectorizerDriver._vectorizer_model.predict([vector])
      return vectorized[0].tolist()
    except Exception as error:
      error_message = f'LocalVectorizerDriver.vectorize: {error}'
      self.logger.log_error(error_message, error)