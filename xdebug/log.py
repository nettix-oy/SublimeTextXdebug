import sublime

import logging
import os

# Settings variables
try:
    from . import settings as S
except:
    import settings as S

# Config module
from .config import get_value


def clear_output():
    # Configure logging module
    output_file = os.path.join(sublime.packages_path(), 'User', S.FILE_LOG_OUTPUT)
    # The values for filemode are the same as for PHP's fopen()
    # a = Open for writing only; place the file pointer at the end of the file. If the file does not exist, attempt to create it.
    logging.basicConfig(filename=output_file, filemode='a', level=logging.DEBUG, format='[%(asctime)s] %(levelname)s - %(message)s', datefmt='%m/%d/%Y %I:%M:%S%p')


def debug(message=None):
    if not get_value(S.KEY_DEBUG) or message is None:
        return
    # Write message to output file
    logging.debug(message)


def info(message=None):
    if message is None:
        return
    # Write message to output file
    logging.info(message)