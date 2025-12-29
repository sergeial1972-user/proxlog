#imports
import requests
from pathlib import Path
from dotenv import load_dotenv

#dotenv
load_dotenv()

def logs_read():
    file_paths = []
    log_dir = Path('/var/log')
    if log_dir.exists() and log_dir.is_dir():
        for file in log_dir.rglob('*'):
            if file.is_file():
                file_paths.append(file)
    log_contents = {}
    for file_path in file_paths:
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
                log_contents[file_path.name] = content
                return log_contents
        except Exception as e:
            print(e)

    return log_contents

logs_read()