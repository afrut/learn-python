# python main.py
# exec(open("main.py").read())

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

if __name__ == "__main__":
    m.add(2, 3) # Run a function from an imported module
    m.some_global_var + 3 # Access a global variable in an imported module
    dir(m)  # See the names that a module defines
    dir() # See names defined currently
    dir(builtins) # See builtin/default names/keywords/functions/etc
    
    # ----------------------------------------
    #  Import search paths
    # ----------------------------------------
    # When importing a module, this is searched first for the module.
    sys.builtin_module_names

    # If not found, then this path is searched next
    sys.path
