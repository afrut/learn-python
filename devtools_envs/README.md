# Background

Many tools exist to streamline Python development workflows including project
dependency management, linting, type checking, etc. Tools and patterns are
listed in the following sections.

# Tools

## Dependency Management

- A _requirements.txt_ file contains dependencies currently installed. It is the
  simplest way to document dependencies.
  ```
  pip freeze >> requirements.txt # Dump currently installed packages into a file
  pip install -r requirements.txt # Install packages listed in a file
  ```
- _Virtual environments_ are used to isolate dependencies and avoid
  version conflicts between multiple projects. See \_venv.
  - Create activate a virtual environment, activate it, and install dependencies.
  ```
  python -m venv env
  source env/bin/activate # env\Scripts\activate for windows
  pip install -r requirements.txt
  ```
- _pip-tools_ can be used to pin the versions of all packages required by a
  top-level package. See \_pip-tools.
- _pipx_ is used to manage the virtual environments of packages that provide a
  command line tool meant to be accessed globally via the PATH environment
  variable. See \_pipx.
- _pyenv_ can be used to manage python versions. See \_pyenv.
- _pyenv-virtualenv_ can be used to manage python versions and virtual
  environments together. See \_pyenv-virtualenv.
- _pipenv_ is a project-level dependency management tool. It manages package
  installations, dependencies, and virtual environments for a given project. See
  \_pipenv.

## Development

- _black_ is a code formatter. See \_black.
- _flake8_ is a linter. See \_flake8.
- _isort_ automatically organizes imports. See \_isort.
- _mypy_ is a static type-checker. See \_mypy.
- If using Visual Studio Code, dedicated extensions for these tools are available.

# Patterns and Setups

- Always use _pipx_ to install Development tools like black meant for global access.
- A _requirements.txt_ and _venv_ can be enough for simple
  applications/sandboxes contained in a directory.
- _pip-tools_, _pyenv_ and _pyenv-virtualenv_ can be used to pin package dependencies,
  manage Python versions, package dependencies and virtual environments.
  - Alternatively, _pipenv_ can also be used to the same effect. If source code
    is self-contained in a single project directory, prefer using pipenv.

# Miscellaneous

- Uninstall all Python packages
  ```
  pip freeze | xargs pip uninstall -y
  ```
- Uninstall all Python packages except `some_package` and `another_package`
  ```
  pip freeze | grep -Ev "(some_package|another_package)" | xargs pip uninstall -y
  ```

# Links

- [Installation guide](https://packaging.python.org/en/latest/tutorials/installing-packages/)
- [Installing standalone command line tools](https://packaging.python.org/en/latest/guides/installing-stand-alone-command-line-tools/)
- [Managing dependencies](https://packaging.python.org/en/latest/tutorials/managing-dependencies/#managing-dependencies)
