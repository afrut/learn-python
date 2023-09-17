- Install and update tools that manage python packages.
  - *pip* is for installing packages.
  - *setuptools* is used fro installing from source code.
  - *wheels* are pre-built binary package format for modules and libraries.
  - The following command will install these packages to the system-wide
    *site-packages* directory.
    - On Windows, it is located in */path/to/python/installation/Lib/site-packages*.
  ```
  python3 -m pip install --upgrade pip setuptools wheel
  ```
- User installation of a package to avoid breaking system-wide packages.
  Installs to a user-specific location.
  - On Windows, installs to *C:\Users\user\appdata\roaming\python\pythonVersion\site-packages*.
  ```
  pip install --user some_package
  ```
- Install a package from local source in development mode.
  ```
  pip install -e <path_to_source_code>
  ```
- A *requirements.txt* file contains dependencies.
  ```
  pip freeze >> requirements.txt
  ```
- *Virtual environments* are used to isolate project dependencies and avoid
  version conflicts between multiple projects. See _venv.
  - Create activate a virtual environment, activate it, and install dependencies.
  ```
  python -m venv env
  source env/bin/activate # env\Scripts\activate for windows
  pip install -r requirements.txt
  ```
- *pipx* is used to manage the virtual environments of packages that provide a
  command line tool meant to be accessed globally via the PATH environment
  variable. See _pipx. 
- *pipenv* is a project-level dependency management tool. It manages package
  installations, dependencies, and virtual environments for a given project. See
  _pipenv.
- *pyenv* can be used to manage python versions. See _pyenv.

# Links
- [Packaging Guide](https://packaging.python.org/en/latest/)
- [Packaging Overview](https://packaging.python.org/en/latest/overview/)
- [Installation guide](https://packaging.python.org/en/latest/tutorials/installing-packages/)
- [Installing standalone command line tools](https://packaging.python.org/en/latest/guides/installing-stand-alone-command-line-tools/)
- [Managing dependencies](https://packaging.python.org/en/latest/tutorials/managing-dependencies/#managing-dependencies)
- [Packaging Python projects](https://packaging.python.org/en/latest/tutorials/packaging-projects/#)
- [Packaging and distributing projects](https://packaging.python.org/en/latest/guides/distributing-packages-using-setuptools/#distributing-packages)