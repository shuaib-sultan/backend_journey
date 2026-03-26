import logging
from logging.handlers import RotatingFileHandler
import os
#it's function to setup the logger and create it in  the right folder .
def setup_logger():
    logger = logging.getLogger("app_logger")# to create the logger with app_logger name .
    logger.setLevel(logging.DEBUG) # to set level of logger debug is include all the leveles.
    log_folder = "logs" # the name of folder.
    os.makedirs(log_folder, exist_ok=True) #cerate the folder if not exsits
    log_file = os.path.join(log_folder, "app.log") # the path of file and cerate it .
    handler = RotatingFileHandler(log_file, maxBytes=500000, backupCount=5) # to make the file max size is 500kbyt
    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s"
    )#to format the masseges and the things
    handler.setFormatter(formatter) # excute the format you do .
    logger.addHandler(handler) # addd handler to the main logger
    return logger
