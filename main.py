#imports
import logging
import configparser
import requests

# Configure logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Create handlers
file_handler = logging.FileHandler('app.log')  # file handler
file_handler.setLevel(logging.INFO)

stream_handler = logging.StreamHandler()  # console handler
stream_handler.setLevel(logging.INFO)

# Create formatters and add to handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
stream_handler.setFormatter(formatter)

# Add handlers to the logger
logger.addHandler(file_handler)
logger.addHandler(stream_handler)

# Read config from file
config = configparser.ConfigParser()
config.read("config.ini")

endpoint = config['connection']['endpoint']
sending_frequency = config['sender']['sending_frequency']

def log_read():
    with open("/var/log/syslog", "r", encoding="utf-8") as syslog:
        syslog_content = syslog.read()
    logger.info("Syslog successfully read")
    return syslog_content

def log_send():
    url = endpoint
    content = log_read()
    response = requests.post(url, data={'file_content': content})
    if response.ok:
        logger.info("Log successfully sent")
    else:
        logger.error(f"Failed to send log: {response.status_code}")

if __name__ == "__main__":
    log_send()
