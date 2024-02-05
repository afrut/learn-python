# The presence of this file makes python treat all directories in the directory
# of this file as other packages.

# A package variable that can be imported by from my_package import package_var
package_var = 3

# from my_package_module import * imports only package_module 
__all__ = ["package_module"]