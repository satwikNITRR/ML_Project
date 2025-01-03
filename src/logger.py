import logging
import os
from datetime import datetime

# Create a directory for logs
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_dir = os.path.join(os.getcwd(), "logs")  # Logs directory
os.makedirs(logs_dir, exist_ok=True)  # Ensure the directory exists

# Complete path for the log file
LOG_FILE_PATH = os.path.join(logs_dir, LOG_FILE)

# Configure logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

if __name__ == '__main__':
    print(os.getcwd())
    # logging.info("Hello dosto")
    # logging.warning("WARNINNNNGNGNGNGN")
