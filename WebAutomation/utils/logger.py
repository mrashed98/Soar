import logging
import functools
from datetime import datetime

def log_action(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        logger = logging.getLogger('playwright_tests')
        class_name = args[0].__class__.__name__
        method_name = func.__name__
        
        logger.info(f"Starting {class_name}.{method_name}")
        try:
            result = func(*args, **kwargs)
            logger.info(f"Completed {class_name}.{method_name}")
            if result is not None:
                logger.info(f"Result: {result}")
            return result
        except Exception as e:
            logger.error(f"Error in {class_name}.{method_name}: {str(e)}")
            raise
    return wrapper