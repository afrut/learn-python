# This is a module. It can contain entities like classes, functions, variables,
# etc. It can be imported by other scripts and modules by using the import
# keyword.

some_global_var = 7

def add(x: int, y: int):
    return x + y

def sub(x: int, y: int):
    return x - y

# In addition to being imported into other modules, all code in the next block
# will be executed when this module is run as a script, ie `python
# my_module.py`, but will not be run when importing.
if __name__ == "__main__":
    add(3, 2)