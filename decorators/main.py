import logging
from functools import wraps
from time import perf_counter, sleep
from typing import Callable, Tuple, Type

# Format for timestamp and logging message
fmt = "%(pathname)s:%(lineno)d: %(message)s"
logging.basicConfig(format=fmt, level=logging.INFO)


def add_3d_vectors(
    x: Tuple[int, int, int], y: Tuple[int, int, int]
) -> Tuple[int, int, int]:
    return (x[0] + y[0], x[1] + y[1], x[2] + y[2])


# Functions are objects in Python and can be stored in variables
f = add_3d_vectors
tpl3d1 = (1, 1, 1)
tpl3d2 = (2, 2, 2)
f(tpl3d1, tpl3d2)  # returns (3, 3, 3)


# Functions can return functions
def print_return_before_returning(func: Callable) -> Callable:
    # This function modifies the function passed in
    def wrapper(*args, **kwargs):
        ret = func(*args, **kwargs)
        logging.info(ret)
        return ret

    return wrapper


# region Functions that return functions can be chain-called like this
# prints (3, 3, 3) and returns (3, 3, 3)
print("Functions that return functions")
print_return_before_returning(add_3d_vectors)(tpl3d1, tpl3d2)

# Get a version of a function that prints the return before returning
add_3d_vectors = print_return_before_returning(add_3d_vectors)
add_3d_vectors(tpl3d1, tpl3d2)  # prints (3, 3, 3) and returns (3, 3, 3)
print("")
# endregion


# region The same function as print_before_returning but uses the wraps
# decorator
print("Using the wraps decorator")


def print_return(func: Callable) -> Callable:
    # The wraps decorator preserves the original function's introspection
    # metadata, like __name__
    @wraps(func)
    def wrapper(*args, **kwargs):
        ret = func(*args, **kwargs)
        logging.info(ret)
        return ret

    return wrapper


# Instead of calling a function that returns a function, decorators can be used
@print_return
def add_2d_vectors(x: Tuple[int, int], y: Tuple[int, int]) -> Tuple[int, int]:
    return (x[0] + y[0], x[1] + y[1])


# Prints (3, 3) before returning (3, 3)
tpl2d1 = (1, 1)
tpl2d2 = (2, 2)
add_2d_vectors(tpl2d1, tpl2d2)

# Using wraps decorator
add_3d_vectors.__name__  # value is "wrapper", because wrapper calls add_3d_vectors
add_2d_vectors.__name__  # value is "add_2d_vectors" because of @wraps decorator
print("")
# endregion


# region A simple decorator pattern
def simple_decorator(func: Callable):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Do something before calling func
        ret = func(*args, **kwargs)
        # Do something after calling func
        return ret

    return wrapper


# endregion


# region A decorator that takes in an argument
# Note that it has 2 outer functions that return functions
print("Decorators that take an argument")


def repeat_log_before_returning(num: int) -> Callable:
    """
    Repeats the log before returning
    """

    def log_before_returning(func) -> Callable:
        """
        Logs before returning as a demonstration function
        """

        @wraps(func)
        def wrapper(*args, **kwargs):
            ret = func(*args, **kwargs)
            for _ in range(num):
                logging.info(f"Logging before returning {ret}")
            return ret

        return wrapper

    return log_before_returning


# It can be chained like this
repeat_log_before_returning(3)(add_2d_vectors)(tpl2d1, tpl2d2)

f = repeat_log_before_returning(3)  # f is def log_before_returning(func) -> Callable
g = f(add_2d_vectors)  # g is def wrapper(*args, **kwargs)
h = g(tpl2d1, tpl2d2)  # h is (3, 3)
print("")

print("Using decorators that take arguments")


# Use it as a decorator to repeat the log of the return before returning
@repeat_log_before_returning(num=7)
def add_2d_vectors_decorated(x, y):
    return (x[0] + y[0], x[1] + y[1])


# This will log the return 7 times before returning
add_2d_vectors_decorated(tpl2d1, tpl2d2)

print("")
# endregion


# region Keeping state in a function using function attributes
def count_calls(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.number_of_times_called += 1
        return func(*args, **kwargs)

    wrapper.number_of_times_called = 0  # type: ignore
    return wrapper


@count_calls
def print_foo():
    print("foo")


print("Keeping state in a function")
for _ in range(5):
    print_foo()
print(print_foo.number_of_times_called)  # type: ignore

print("")
# endregion


# region Implementing a singleton decorator can be used to ensure only 1
# instance of a class is instantiated
def singleton(cls: Type):
    """
    Takes a class. When a class is invoked, its constructor/initializer is called
    """

    @wraps(cls)
    def wrapper(*args, **kwargs):
        if wrapper.class_instance is None:
            wrapper.class_instance = cls(*args, **kwargs)
        return wrapper.class_instance

    wrapper.class_instance = None  # type: ignore

    return wrapper


class SomeClass:
    def __init__(self):
        pass


@singleton
class SingletonClass:
    def __init__(self):
        pass


someclass1 = SomeClass()
someclass2 = SomeClass()
singletonclass1 = SingletonClass()
singletonclass2 = SingletonClass()


print("Singletons")
print(f"id(someclass1) == id(someclass2): {id(someclass1) == id(someclass2)}")
print(f"someclass1 is someclass2: {someclass1 is someclass2}")
print(
    f"id(singletonclass1) == id(singletonclass2): {id(singletonclass1) == id(singletonclass2)}"
)
print(f"singletonclass1 is singletonclass2: {singletonclass1 is singletonclass2}")

print("")
# endregion


# region Timing function
def timer(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = perf_counter()
        ret = func(*args, **kwargs)
        wrapper.elapsed = perf_counter() - start_time
        print(f"{func.__name__} took {wrapper.elapsed:.6f}s")
        return ret

    return wrapper


@timer
def lazy_func():
    sleep(3)


print("Timing functions")
lazy_func()
print("")

# endregion

# See json_schema_validation.py for validating input dict schemas.

# decorators that take 0 or keyword args
# nesting decorators
# chaining decorators
# classes as decorators with __call__

# debugging code
# rate limiting code
# registering plugins
# authentication and authorization (flask)
# stateful decorators - call counters
# caching return values
# adding information - eg, units
# validating inputs

# Deco
# ShowMe
