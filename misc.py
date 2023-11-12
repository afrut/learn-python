import sys


class MyClass:
    some_attr: int = 0

    def __init__(self, x):
        self.x = x


def func():
    x = 1
    # Returns a dict where keys are variable names and values are the values of
    # the variables.
    # In this case, vars_in_scope  = {"x": 1}
    vars_in_scope = locals()


if __name__ == "__main__":
    # Get the value of an object's attribute
    print(getattr(MyClass, "some_attr"))

    # Reference a class by a string
    cls = getattr(sys.modules[__name__], "MyClass")
    mc = cls(55)
    mc.x  # value of x for an instance of MyClass
