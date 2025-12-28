import os # Used for filesystem operations (paths, folders).
import sys # Used to access system-level objects (here: stdout)
import logging # Python’s built-in logging module.

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"
log_dir = "logs"
log_filepath = os.path.join(log_dir,"running_logs.log")
os.makedirs(log_dir, exist_ok=True) # Create if not existed

logging.basicConfig(
    level = logging.INFO, # Logs INFO and above: INFO, WARNING, ERROR, CRITICAL, not DEBUG
    format = logging_str,
    handlers = [
        logging.FileHandler(log_filepath), # Writes logs to logs/running_logs.log
        logging.StreamHandler(sys.stdout)  # Prints logs to the terminal
    ]
)

logger = logging.getLogger("textSummarizerLogger") # Creates a custom logger instance