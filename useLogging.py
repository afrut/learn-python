# python useLogging.py
import logging

if __name__ == "__main__":
    # Format for timestamp and logging message
    fmt = "%(asctime)s.%(msecs)03d: %(message)s"
    # fmt = "%(pathname)s:%(lineno)d: %(message)s" # path of the file with line number of every log
    datefmt = "%Y-%m-%d %H:%M:%S"
    logging.basicConfig(format=fmt, level=logging.INFO, datefmt=datefmt)
    logging.info("hello world")
