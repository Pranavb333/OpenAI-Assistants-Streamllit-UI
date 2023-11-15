import time

from util.logger import logger


def time_and_log(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        logger.info(f"{func.__name__} took {execution_time} seconds")
        return result

    return wrapper


def log_message_length(message_type: str, message: str):
    message_length = len(message.split())

    logger.info(f"{message_type} is {message_length} words")
