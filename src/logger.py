import logging  # keep track of any information file
import os  # file handling
from datetime import datetime

# Generate log file name based on current date and time
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Create the directory path for storing log files
logs_path = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_path, exist_ok=True)

# Full path for the log file
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# Set up basic configuration for logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

# Example usage:
#logging.info("Logging system is set up correctly!")
