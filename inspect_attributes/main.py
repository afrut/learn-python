# It can be convenient to inspect the attributes of a class. This file shows a
# few different ways.

from __future__ import annotations

import inspect
from typing import Iterable, List, Tuple


def _print(it: Iterable, header: str, ignore_magic: bool = True):
    print(header)
    for x in it:
        if isinstance(x, tuple):
            name = x[0]
        else:
            name = x

        if ignore_magic and name.startswith("__"):
            # Ignore magic methods
            continue
        print(f"    {x}")


class Vector3D:
    origin = (0, 0, 0)

    def __init__(self, x: float = 0, y: float = 0, z: float = 0):
        self.x = x
        self.y = y
        self.z = z

    def add(self, v: Vector3D) -> Vector3D:
        return Vector3D(x=self.x + v.x, y=self.y + v.y, z=self.z + v.z)

    def dot_product(self, v: Vector3D) -> float:
        return sum([self.x * v.x, self.y + v.y, self.z + v.z])


if __name__ == "__main__":
    v = Vector3D()

    # Use the dir function
    # Returns methods and class variables
    xs: List[str] = dir(Vector3D)
    # Returns methods, class variables and instance variables
    xs2: List[str] = dir(v)
    _print(xs, "dir(Vector3D)")
    _print(xs2, "dir(v)")

    # Use inspect.getmembers. This gives more information since it also returns
    # the attribute's name and value.
    # Returns class variables and methods only
    xs: List[Tuple[str]] = inspect.getmembers(Vector3D)
    # Returns class variables, methods and instance variables
    xs2: List[Tuple[str]] = inspect.getmembers(v)
    _print(xs, "inspect.getmembers(Vector3D)")
    _print(xs2, "inspect.getmembers(v)")

    # Use the __dict__ magic method
    # __dict__ returns mappingproxy, which is just a dict that has str keys and
    # is read-only. The key is attribute name and the value is the attribute
    # value.
    # Returns class variables and methods only
    xs = Vector3D.__dict__
    # Returns instance variables only
    xs2 = v.__dict__
    _print(xs, "Vector3D.__dict__")
    _print(xs2, "Vector3D.__dict__")

    # Use vars() function. Also returns mappingproxy.
    # Returns class variables and methods only
    xs = vars(Vector3D)
    # Returns instance variables only
    xs2 = vars(v)
    _print(xs, "vars(Vector3D)")
    _print(xs2, "vars(v)")
