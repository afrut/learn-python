# Import a module in the same sub-package
from my_package.sub_package import sub_package_module as spm

# Import a module in a different package
from my_package import package_module as pm

if __name__ == "__main__":
    spm.spm_foo()
    pm.package_module_foo()