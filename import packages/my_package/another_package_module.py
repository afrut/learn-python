# python3 -m my_package.another_package_module
# import a module in the same package
from my_package.package_module import package_module_foo

def another_package_module_foo():
    return(package_module_foo())

if __name__ == "__main__":
    import os
    print(another_package_module_foo() + " from " + os.path.basename(__file__))