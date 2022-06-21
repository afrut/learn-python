#python useLogging.py
import logging

if __name__ == "__main__":
    # Format for timestamp and logging message
    fmt = "%(asctime)s: %(message)s"
    datefmt = "%Y-%m-%d %H:%M:%S"
    logging.basicConfig(format = fmt, level = logging.INFO, datefmt = datefmt)
    logging.info("hello world")