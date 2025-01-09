import os
from datetime import datetime
from loguru import logger

def setup_logger():
    # Setting up the directory for logs
    log_directory = "logs/"
    if not os.path.exists(log_directory):
        try:
            os.makedirs(log_directory)
        except Exception as e:
            print(f"Failed to create log directory: {e}")
            return

    # Configuring loguru logger
    current_time = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    filename = f"{log_directory}/test_log_{current_time}.log"

    # Define the format for the logger
    # Including 'exception' in the format ensures that exception tracebacks are logged when using logger.exception()
    log_format = "{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message} | {file}:{function}:{line} | {exception}"

    try:
        # Add the log file handler with specified rotation and compression settings
        logger.add(filename, rotation="10 MB", compression="zip", level="DEBUG", format=log_format)
    except Exception as e:
        print(f"Failed to add log file handler: {e}")

# Call setup_logger to initialize the logger configuration when this module is imported
setup_logger()