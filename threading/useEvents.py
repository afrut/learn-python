#python threading\\useEvents.py
# Use events to communicate with threads
# In this script, events are used to kill threads
import logging
import time
import threading

# Function to run in threads
def func(name: str, ts: int, stop: threading.Event):
    logging.info(f"Thread {name} starting.")
    while True:
        logging.info(f"Thread {name} executing.")
        time.sleep(ts)
        if stop.is_set():
            break
    logging.info(f"Thread {name} finished.")

if __name__ == "__main__":
    # Format for timestamp and logging message
    fmt = "%(asctime)s: %(message)s"
    datefmt = "%Y-%m-%d %H:%M:%S"

    # Configure logging
    logging.basicConfig(format = fmt, level = logging.INFO, datefmt = datefmt)

    # Create multiple threads
    threadP = [("spam", 2)
        ,("ham", 2)
        ,("eggs", 3)
        ,("bacon", 3)
        ,("toast", 5)]
    threads = dict()
    for tpl in threadP:
        stopEvent = threading.Event()
        threads[tpl[0]] = (threading.Thread(target = func, args = (tpl[0], tpl[1], stopEvent)), stopEvent)

    for threadName in threads:
        threads[threadName][0].start()

    time.sleep(3)
    for threadName in threads:
        threads[threadName][1].set()

    for threadName in threads:
        threads[threadName][0].join()

    logging.info(f"*** All done. ***")