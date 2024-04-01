from multiprocessing import Pool
from time import perf_counter_ns


def is_prime(x: int) -> bool:
    """
    Very naive implementation to check if a number is prime
    """
    for n in range(1, x):
        if x % n == 0:
            return True
    return False


if __name__ == "__main__":
    end_num = 5 * 10**7

    # Execute in one process, on one CPU
    start = perf_counter_ns()
    for x in range(end_num):
        is_prime(x)
    print(f"Single process took {(perf_counter_ns() - start)/1e9}s")

    # Execute in at most 2 processes, on at most 2 CPUs
    # Pool 2 creates a pool of 2 processes that can be used to execute the
    # function
    with Pool(2) as p:
        start = perf_counter_ns()
        p.map(is_prime, range(end_num))
    print(f"Multiprocess 2 took {(perf_counter_ns() - start)/1e9}s")

    # Execute in at most 3 processes, on at most 3 CPUs
    with Pool(3) as p:
        start = perf_counter_ns()
        p.map(is_prime, range(end_num))
    print(f"Multiprocess 3 took {(perf_counter_ns() - start)/1e9}s")
