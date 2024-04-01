# Start Here
- Read programs in the following order:
    - async_basic.py: Contrast synchronous vs asynchronous programming

# Notes
- Coroutines are defined by `async def some_coroutine()`. These can `await`
- `await some_coroutine()` pauses execution of the current coroutine until
  `some_coroutine()` completes.
- Look for modules that support asynchronous operations. For example, the
  `requests` module does not suppor asynchronicity but `aiohttp`. `aiofiles` is
  another module that supports asynchronous file access.

# Resources
- https://realpython.com/async-io-python/#the-asyncio-package-and-asyncawait