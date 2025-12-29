#imports
import requests
from pathlib import Path
from dotenv import load_dotenv

#dotenv
load_dotenv()

def logs_read():
    log_files = []
    log_dir = Path('var/log')
    if log_dir.exists() and log_dir.is_dir():



logs_read()`