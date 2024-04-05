import logging
from functools import wraps
from typing import Callable, Tuple

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


# endregion


# # Repeat the function 7 times
# @repeat(num=7)
# def add_2d_vectors_decorated(x: Tuple[int, int], y: Tuple[int, int]) -> Tuple[int, int]:
#     return (x[0] + y[0], x[1] + y[1])


# print(add_2d_vectors_decorated((1, 1), (2, 2)))


# See json_schema_validation.py for validating input dict schemas.

# decorators that take 0 or keyword args
# nesting decorators
# chaining decorators
# classes as decorators with __call__

# timing functions
# debugging code
# rate limiting code
# registering plugins
# authentication and authorization (flask)
# stateful decorators - call counters
# creating singletons
# caching return values
# adding information - eg, units
# validating inputs

# Deco
# ShowMe
