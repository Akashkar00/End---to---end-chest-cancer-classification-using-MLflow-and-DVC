import os
import sys
import logging

# Log format
LOG_FORMAT = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

# Log file setup
LOG_DIR = "logs"
LOG_FILEPATH = os.path.join(LOG_DIR, "running_logs.log")
os.makedirs(LOG_DIR, exist_ok=True)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format=LOG_FORMAT,
    handlers=[
        logging.FileHandler(LOG_FILEPATH),
        logging.StreamHandler(sys.stdout)
    ]
)

# Create logger
logger = logging.getLogger("cnnClassifierLogger")