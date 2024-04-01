- `pyenv-virtualenv` is a `pyenv` plugin that manages Python versions
  automatically with virtual environments and dependencies.
- `pyenv-virtualenv` is only available for UNIX-like systems.
- [pyenv-virtualenv Project Page](https://github.com/pyenv/pyenv-virtualenv)

# Usage
- Create a virtualenv with a specific version of Python
  ```
  pyenv virtualenv 3.10.4 my-env
  ```
- List existing virtualenvs created
  ```
  pyenv virtualenvs
  ```
- Activate a virtualenv
  ```
  pyenv activate my-env
  ```
- Deactivate
  ```
  pyenv deactivate
  ```
- Create a file that causes pyenv-virtualenv to automatically activate an
  enviroment
  ```
  pyenv local
  ```