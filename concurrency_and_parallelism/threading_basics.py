# python threading\\useThreads.py
import logging
import threading
import time


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
    logging.basicConfig(format=fmt, level=logging.INFO, datefmt=datefmt)

    # Create 2 threads; one will sleep for 1 second, the other for 2
    thd1 = threading.Thread(target=func, args=("sample1", 1))
    thd2 = threading.Thread(target=func, args=("sample2", 2))

    # Start both threads
    thd2.start()
    thd1.start()

    # Wait for both threads to complete
    thd1.join(5)
    thd2.join(5)

    # Create multiple threads
    threadP = [
        ("spam", 2, False),
        ("ham", 2, False),
        ("eggs", 2, False),
        ("bacon", 5, True),
        ("toast", 3, True),
    ]
    threads = {
        tpl[0]: threading.Thread(
            target=func,
            args=(
                tpl[0],
                tpl[1],
            ),
            daemon=tpl[2],
        )
        for tpl in threadP
    }
    for name in threads:
        threads[name].start()

    # Note that by default, Python waits for all non-daemon threads to complete
    # before terminating the main thread. Daemon threads are automatically
    # terminated when the main thread completes. Note that thread bacon does not
    # complete.

    # Wait for a thread to complete. If this is not here, thread toast will not
    # complete since it is a daemon thread. Thread bacon still does not complete.
    logging.info("Joining to thread toast in main thread")
    threads["toast"].join()

    # Note that thread bacon does not complete but terminates because the main
    # thread completes.
