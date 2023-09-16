from . import sub_package_module as spm
from .. import package_module as pm
from ..package_module import package_module_foo

def foo():
    return spm.spm_foo()

def bar():
    return package_module_foo()

def baz():
    return pm.package_module_bar()