import logging
import os
import sys
import traceback
import linecache

from datetime import datetime
from typing import Optional

from ...core.ports.logger_port import LoggerPort

class LoggerDriver(LoggerPort):
  _instance = None
  
  def __new__(cls):
    if not cls._instance:
      cls._instance = super(LoggerDriver, cls).__new__(cls)
      cls._instance._initialize()
    return cls._instance


  def _initialize(self) -> None:
    self.logger = logging.getLogger(__name__)
    self.logger.setLevel(logging.DEBUG)
    
    curr_dir = os.getcwd()
    log_dir = os.path.join(curr_dir, 'logs')
      
    if not os.path.exists(log_dir):
      os.makedirs(log_dir)
    
    log_file=f'bank_log_{datetime.now().strftime("%Y-%m-%d")}.log'
    
    log_path = os.path.join(log_dir, log_file)
    self.log_path = log_path
    
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    
    file_handler = logging.FileHandler(log_path, mode='a')
    file_handler.setFormatter(formatter)
    self.logger.addHandler(file_handler)
    
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    self.logger.addHandler(console_handler)

  def log_info(self, message: str = 'None') -> None:
    self.logger.info(message)


  def log_error(self, message: str = 'None', error: Optional[Exception] = None) -> None:
    trace_error = 'None'
    
    if error is not None:
      tb = traceback.extract_tb(error.__traceback__)
      
      traces = []
      for frame in tb:
        code_snippet = linecache.getline(frame.filename, frame.lineno)
        trace = f'>>> file: {frame.filename}, line: {frame.lineno}\n--- {code_snippet.strip()}'
        traces.append(trace)
        
      trace_error = '\n'.join(traces)
      
    self.logger.error(f'{message}\n{trace_error}')
    sys.exit(1)


  def close_logger(self) -> None:
    for handler in self.logger.handlers:
      handler.close()