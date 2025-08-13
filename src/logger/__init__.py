import os
import logging
from logging.handlers import RotatingFileHandler
from from_root import from_root
from datetime import datetime

LOG_DIR = 'logs'
LOG_FILE = f"{LOG_DIR}/log_{datetime.now().strftime('%Y-%m-%d')}.log"
MAX_LOG_SIZE = 5 * 1024 * 1024  # 5 MB
BACKUP_COUNT = 3

log_dir_path = os.path.join(from_root(), LOG_DIR)
os.makedirs(log_dir_path, exist_ok=True)
log_file_path = os.path.join(log_dir_path, LOG_FILE)

def configure_logger():
    # Create Logger
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    # Create Handler
    handler = RotatingFileHandler(log_file_path, maxBytes=MAX_LOG_SIZE, backupCount=BACKUP_COUNT)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    # Create Console Handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    console_handler.setLevel(logging.INFO)

    # Add Handler to Logger
    logger.addHandler(handler)
    logger.addHandler(console_handler)


configure_logger()