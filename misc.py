import sys


class MyClass:
    some_attr: int = 0

    def __init__(self, x):
        self.x = x


if __name__ == "__main__":
    # Get the value of an object's attribute
    print(getattr(MyClass, "some_attr"))

    # Reference a class by a string
    cls = getattr(sys.modules[__name__], "MyClass")
    mc = cls(55)
    mc.x  # value of x for an instance of MyClass
