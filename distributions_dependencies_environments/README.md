- Install and update tools that manage python packages.
  - *pip* is for installing packages.
  - *setuptools* is used fro installing from source code.
  - *wheels* are pre-built binary package format for modules and libraries.
  ```
  python3 -m pip install --upgrade pip setuptools wheel
  ```
- User installation of a package to avoid breaking system-wide packages.
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
- Some packages provide tools that must be accessible globally via the command
  line. *pipx* creates virtual environments for these tools and makes sure they
  are accessible via the PATH variable.
  - Some useful ones are *black*, *flake8*, *mypy*, *isort*, and *pipenv*.
  ```
  pip install pipx
  pipx install black
  pipx upgrade black
  pipx run black some_script.py
  pipx list # see what is installed
  ```
* *pipenv* is a project-level dependency management tool. It manages package
  installations, dependencies, and virtual environments for a given project.
* *pyenv* can be used to manage python versions. See _pyenv.