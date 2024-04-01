# Background
Many tools exist to streamline Python development workflows including project
dependency management, linting, type checking, etc. Tools and patterns are
listed in the following sections.

# Tools
## Dependency Management
- A *requirements.txt* file contains dependencies currently installed. It is the
  simplest way to document dependencies.
  ```
  pip freeze >> requirements.txt # Dump currently installed packages into a file
  pip install -r requirements.txt # Install packages listed in a file
  ```
- *Virtual environments* are used to isolate dependencies and avoid
  version conflicts between multiple projects. See _venv.
  - Create activate a virtual environment, activate it, and install dependencies.
  ```
  python -m venv env
  source env/bin/activate # env\Scripts\activate for windows
  pip install -r requirements.txt
  ```
- *pip-tools* can be used to pin the versions of all packages required by a
  top-level package. See _pip-tools.
- *pipx* is used to manage the virtual environments of packages that provide a
  command line tool meant to be accessed globally via the PATH environment
  variable. See _pipx. 
- *pyenv* can be used to manage python versions. See _pyenv.
- *pyenv-virtualenv* can be used to manage python versions and virtual
  environments together. See _pyenv-virtualenv.
- *pipenv* is a project-level dependency management tool. It manages package
  installations, dependencies, and virtual environments for a given project. See
  _pipenv.

## Development
- *black* is a code formatter. See _black.
- *flake8* is a linter. See _flake8.
- *isort* automatically organizes imports. See _isort.
- *mypy* is a static type-checker. See _mypy.
- If using Visual Studio Code, dedicated extensions for these tools are available.

# Patterns and Setups
- Always use *pipx* to install Development tools like black meant for global access.
- A *requirements.txt* and *venv* can be enough for simple
  applications/sandboxes contained in a directory.
- *pip-tools*, *pyenv* and *pyenv-virtualenv* can be used to pin package dependencies,
  manage Python versions, package dependencies and virtual environments.
  - Alternatively, *pipenv* can also be used to the same effect. If source code
    is self-contained in a single project directory, prefer using pipenv.

# Links
- [Installation guide](https://packaging.python.org/en/latest/tutorials/installing-packages/)
- [Installing standalone command line tools](https://packaging.python.org/en/latest/guides/installing-stand-alone-command-line-tools/)
- [Managing dependencies](https://packaging.python.org/en/latest/tutorials/managing-dependencies/#managing-dependencies)