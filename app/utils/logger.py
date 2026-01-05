import logging
import sys
from datetime import datetime
import os

def setup_logger():
    """Setup application logging"""
    
    # Create logs directory if it doesn't exist
    log_dir = "app/logs"
    os.makedirs(log_dir, exist_ok=True)
    
    logger = logging.getLogger("image_analysis_api")
    logger.setLevel(logging.INFO)
    
    # Create handlers
    console_handler = logging.StreamHandler(sys.stdout)
    
    log_filename = datetime.now().strftime("image_api_%Y%m%d.log")
    file_handler = logging.FileHandler(os.path.join(log_dir, log_filename))
    
    log_format = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    console_handler.setFormatter(log_format)
    file_handler.setFormatter(log_format)
    
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
    
    return logger

def get_logger(name: str):
    """Get a named logger"""
    return logging.getLogger(f"image_analysis_api.{name}")