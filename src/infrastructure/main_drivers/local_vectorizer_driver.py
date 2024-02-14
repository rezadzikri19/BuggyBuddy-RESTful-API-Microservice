import os
from typing import List

from keras.models import Model, load_model

from ...core.ports.vectorizer_port import VectorizerPort
from ...core.ports.logger_port import LoggerPort

class LocalVectorizerDriver(VectorizerPort):
  def __init__(self, logger: LoggerPort) -> None:
    self.logger = logger

  
  def vectorize(self, vector: List[float]) -> List[float]:
    try:
      curr_dir = os.getcwd()
      data_dir = os.path.join(curr_dir, 'artifacts', 'models')
      
      if not os.path.exists(data_dir):
          os.makedirs(data_dir)
          
          raise Exception('directory not found!')
        
      file_name = 'model_embedding.h5'
      data_path = os.path.join(data_dir, file_name)
      
      vectorizer_model: Model = load_model(data_path)
      revector = vectorizer_model.predict([vector])
      return revector[0].tolist()
    except Exception as error:
      error_message = f'LocalVectorizerDriver.vectorize: {error}'
      self.logger.log_error(error_message, error)