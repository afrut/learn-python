import asyncio
import time
import random
import logging

# time.sleep() and asyncio.sleep() are used to simulate long-running operations.
# In practice, these can be writing large amounts of data to a file, waiting on
# an HTTP request completing, querying a database, performing some heavy
# computation etc.

# A synchronous long-running function. This function will block all other
# execution until it is complete. Then it will give control back to the main
# thread.
def long_running_sync(id: int, ts: int):
    logging.info(f"long_running_sync({id}) going to sleep for {ts}s")
    time.sleep(ts)
    logging.info(f"long_running_sync({id}) complete")

# An asynchronous long-running function. Note the use of await asyncio.sleep().
# The async keyword in the function declaration makes this function a coroutine.
# await pauses execution of the coroutine and gives control back to the event
# loop. When the coroutine finishes the awaited step, the event loop will be
# notified to resume.
async def long_running_async(id: int, ts: int):
    logging.info(f"long_running_async({id}) going to sleep for {ts}s")

    # Return control to the main event loop and allow it to execute other functions.
    await asyncio.sleep(ts)
    logging.info(f"long_running_async({id}) complete")

# The "main" asynchronous function to run the event loop. The main thread (also
# known as event loop) monitors coroutines and executes code when something is
# available.
async def main_async(n: int, ts: int):

    # Build a tuple of coroutines.
    coroutines = (long_running_async(x, ts) for x in range(n))
    
    # Wait for all coroutines to complete.
    await asyncio.gather(*coroutines)

if __name__ == "__main__":
    # Format for timestamp and logging message
    fmt = "%(asctime)s.%(msecs)03d: %(message)s"
    datefmt = "%Y-%m-%d %H:%M:%S"
    logging.basicConfig(format = fmt, level = logging.INFO, datefmt = datefmt)

    # Parameters
    time_to_sleep = 3
    num_tasks = 5

    # Run a synchronous function 5 times
    logging.info("Starting synchronous tasks.")
    tmStart = time.perf_counter()
    for x in range(num_tasks):
        long_running_sync(x, time_to_sleep)
    logging.info(f"Synchronous tasks finished in {time.perf_counter() - tmStart:.2f}s")

    # Run asynchronous coroutines 5 times.
    logging.info("Starting asynchronous event loop.")
    tmStart = time.perf_counter()
    asyncio.run(main_async(num_tasks, time_to_sleep))
    logging.info(f"Asynchronous coroutines completed in {time.perf_counter() - tmStart:.2f}s")