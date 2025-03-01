import logging
from colorama import Fore, Style

def get_logger():
    
    level_of_logging = [logging.DEBUG, logging.INFO, logging.WARNING, logging.ERROR, logging.CRITICAL][0]
    # Create a custom formatter for colored output
    class ColoredFormatter(logging.Formatter):
        def format(self, record):
            # Map log levels to colors
            color_map = {
                logging.DEBUG: Fore.BLUE,
                logging.INFO: Fore.GREEN,
                logging.WARNING: Fore.YELLOW,
                logging.ERROR: Fore.RED,
                logging.CRITICAL: Fore.RED + Style.BRIGHT,
            }
            record.msg = color_map.get(record.levelno, Fore.WHITE) + str(record.msg) + Style.RESET_ALL
            return super().format(record)

    # Configure the logger
    logger = logging.getLogger(__name__)
    logger.setLevel(level_of_logging)

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(ColoredFormatter('%(asctime)s - %(levelname)s - %(filename)s - %(lineno)d - %(message)s'))

    logger.addHandler(stream_handler)
    return logger

logger = get_logger()