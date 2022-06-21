#python useThreads.py
import logging
import time
import threading

# Function to run in threads
def func(name: str, ts: int):
    logging.info(f"Thread {name} starting.")
    time.sleep(ts)
    logging.info(f"Thread {name} finished.")

if __name__ == "__main__":
    # Format for timestamp and logging message
    fmt = "%(asctime)s: %(message)s"
    datefmt = "%Y-%m-%d %H:%M:%S"

    # Configure logging
    logging.basicConfig(format = fmt, level = logging.INFO, datefmt = datefmt)

    # Create multiple threads
    threadP = [("spam", 2, False)
        ,("ham", 2, False)
        ,("eggs", 2, False)
        ,("bacon", 5, True)
        ,("toast", 3, True)]
    threads = {tpl[0]: threading.Thread(target = func, args = (tpl[0], tpl[1],), daemon = tpl[2]) for tpl in threadP}
    for name in threads:
        threads[name].start()

    logging.info(f"*** All done. ***")

    # Note that by default, Python waits for all non-daemon threads to complete
    # before terminating the main thread. Daemon threads are automatically
    # terminated when the main thread completes. Note that thread bacon does not
    # complete.

    # Wait for a thread to complete. If this is not here, thread toast will not
    # complete since it is a daemon thread. Thread bacon still does not complete.
    threads["toast"].join()