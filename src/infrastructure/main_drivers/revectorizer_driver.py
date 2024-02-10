import os
from typing import List

from keras.models import Model, load_model

from ...core.ports.revectorizer_port import RevectorizerPort

class RevectorizerDriver(RevectorizerPort):
  def __init__(self) -> None:
    pass
  
  def revectorize(vector: List[float]) -> List[float]:
    curr_dir = os.getcwd()
    data_dir = os.path.join(curr_dir, 'artifacts', 'model')
    
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
        
        raise Exception('directory not found!')
      
    file_name = 'revectorizer.bin'
    data_path = os.path.join(data_dir, file_name)
     
    revectorizer_model: Model = load_model(data_path)
    revector = revectorizer_model.predict([vector])
    return revector[0]