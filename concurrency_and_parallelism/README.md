# Background
- **Concurrency** refers to the ability of a program to run non-sequentially and
  in an overlapping manner.
- **Parallelism** refers to splitting up operations and executing them simultaneously.
- **IO-bound** operations are sent by the CPU to request operations from the
  disk, an external database, something on the network, an HTTP endpoint, etc.
  The CPU then sits idle until the request completes.
- **CPU-bound** operations require the CPU to do some computations. These
  operations keep the CPU occupied.
- A **process** is a program that has been loaded into memory. It executes on a
  single CPU core.
- A **thread** is a unit of execution within a process. A process can execute
  multiple threads. Threads share the same memory space.
- **Asynchronous** programming allows a program to pause execution to wait on
  an operation, execute something else, then resume execution once the
  operation has returned.
- **Multithreading** uses multiple threads to issue IO-bound operations to
  various resources like disk, external databases, HTTP endpoints, etc.
- **Multiprocessing** spawns multiple processes, each on a separate CPU core,
  to do calculations simultaneously.

# Resources and Links
- [Concurrency](https://en.wikipedia.org/wiki/Concurrency_(computer_science))
- [Parallelism](https://en.wikipedia.org/wiki/Parallel_computing)
- [Multithreading vs Multiprocessing in Python](https://www.geeksforgeeks.org/difference-between-multithreading-vs-multiprocessing-in-python/)
- [Python Concurrency and Parallelism Explained](https://www.infoworld.com/article/3632284/python-concurrency-and-parallelism-explained.html)
- [Async IO in Python: A Complete Walkthrough](https://realpython.com/async-io-python/#the-asyncawait-syntax-and-native-coroutines)
- [Threading in Python](https://docs.python.org/3/library/threading.html)
- [Multiprocessing in Python](https://docs.python.org/3/library/multiprocessing.html)