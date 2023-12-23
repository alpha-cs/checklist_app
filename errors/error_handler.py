# errors/error_handler.py
import logging
import os
import traceback


def setup_logging():
    log_directory = "errors/logs"
    if not os.path.exists(log_directory):
        os.makedirs(log_directory)

    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        filename=os.path.join(log_directory, 'app.log'),
                        filemode='a')


def log_exception():
    """ Log the current exception with traceback information. """
    logging.error("Exception occurred", exc_info=True)


def log_detailed_exception():
    """ Log the current exception with detailed traceback information. """
    exc_info = traceback.format_exc()
    logging.error(f"Exception occurred: {exc_info}")
