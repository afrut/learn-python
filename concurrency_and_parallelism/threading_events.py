# python threading\\useEvents.py
# Use events to communicate with threads
# In this script, events are used to kill threads
import logging
import threading
import time


# Function to run in threads
def func(name: str, ts: int, stop: threading.Event):
    """
    Prints, sleeps, then loop. If stop event is set, terminate loop.
    """
    logging.info(f"Thread {name} starting.")
    n = 0
    while True:
        logging.info(f"Thread {name} executing {n}.")
        time.sleep(ts)
        if stop.is_set():
            break
        n += 1
    logging.info(f"Thread {name} finished.")


if __name__ == "__main__":
    # Format for timestamp and logging message
    fmt = "%(asctime)s: %(message)s"
    datefmt = "%Y-%m-%d %H:%M:%S"

    # Configure logging
    logging.basicConfig(format=fmt, level=logging.INFO, datefmt=datefmt)

    # Create a thread with a stop event
    stop = threading.Event()
    thd = threading.Thread(
        target=func,
        args=("sample", 1, stop),
    )

    # Start the thread and sleep for 10s, then stop the thread using the event
    # The thread will loop approximately 10 times
    thd.start()
    time.sleep(10)
    stop.set()
