import logging
import os
from logging.handlers import RotatingFileHandler
from logging import StreamHandler
def creat_logger_system():
  logger=logging.getLogger("app_logger")
  if logger.handlers:
    return logger
  log_level=os.getenv("LOG_LEVEL","DEBUG")
  level = getattr(logging, log_level.upper(),logging.DEBUG)
  logger.setLevel(level)
  log_folder="logs"
  os.makedirs(log_folder,exist_ok=True)
  log_file=os.path.join(log_folder,"app.log")
  file_size=5 * 1024 * 1024 
  formatter=logging.Formatter(
      f"%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    )
  handler= RotatingFileHandler(log_file,maxBytes=file_size,backupCount=5,encoding="utf-8")
  consol_handler=StreamHandler()
  consol_handler.setFormatter(formatter)
  handler.setFormatter(formatter)
  logger.addHandler(handler)
  logger.addHandler(consol_handler)
  return logger