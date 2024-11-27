import logging
from library.exceptions import CustomError

def handle_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logging.error(f"An error occurred in {func.__name__}: {e}")
            raise CustomError("An unexpected error occurred") from e
    return wrapper
