from loguru import logger
import sys

logger.remove()  # remove default logger
logger.add(sys.stderr, format="{time} {level} {message}", level="INFO")
logger.add("app.log", rotation="1 MB", level="INFO")

def get_logger():
    return logger

