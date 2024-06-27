# python main.py
# Import a module from the directory that main.py is run into the global
# namespace of this module. If a standard module also named my_module exists,
# the module in the current directory takes precedence.
import my_module as m

# Import an entity from the module directly into main.py's global namespace
from my_module import sub

# Import all entities not beginning with "_" in my_module directly into
# main.py's global namespace. This is not encourage as it pollutes the namespace.
from my_module import *

# Reload the module. Start the python interpreter for an interactive session.
# Run main.py using exec(open("main.py").read()). Change my_module. Running
# exec(open("main.py").read()) will NOT re-import my_module. importlib.reload()
# is used to reload the module.
import importlib
importlib.reload(m)

import sys
import builtins

# Import a variable defined in a package
from my_package import package_var

# Import a module defined in a package
from my_package import package_module as pm

# Import a function defined in a module in a package
from my_package.another_package_module import another_package_module_foo

# Import a sub-package defined in a package
from my_package.sub_package import sub_package_module as spm
import my_package.sub_package.sub_package_module as spm2

# Import names in a submodule inside a subpackage
from my_package.sub_package.sub_package_module import spm_foo

# Import a submodule that uses relative imports
from my_package.sub_package.use_relative_imports import foo, bar, baz

if __name__ == "__main__":
    m.add(2, 3) # Run a function from an imported module
    m.some_global_var + 3 # Access a global variable in an imported module
    dir(m)  # See the names that a module defines
    dir() # See names defined currently
    dir(builtins) # See builtin/default names/keywords/functions/etc

    # Use names from a submodule that uses relative imports
    foo(); bar(); baz()
    
    # ----------------------------------------
    #  Import search paths
    # ----------------------------------------
    # When importing a module, this is searched first for the module.
    sys.builtin_module_names

    # If not found, then this path is searched next
    sys.path

    # Access a name in a module inside a package
    pm.package_module_foo()

    # Call a function from a module in a package
    another_package_module_foo()