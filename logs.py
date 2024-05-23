import logging
from logging.handlers import RotatingFileHandler

logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.ERROR,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%m/%d/%Y %H:%M:%S',
    filename='basic.log'
)
# logger.propagate=False

stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)
stream_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s -- stream')
stream_handler.setFormatter(stream_format)

# file_handler = logging.FileHandler('basic.log')
file_handler = RotatingFileHandler('basic.log', maxBytes=1024 * 1024, backupCount=5)
file_handler.setLevel(logging.ERROR)
file_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s -- file')
file_handler.setFormatter(file_format)

logger.addHandler(stream_handler)
logger.addHandler(file_handler)