- Install and update tools that manage python packages.
  - *pip* is for installing packages.
  - *setuptools* is used fro installing from source code.
  - *wheels* are pre-built binary package format for modules and libraries.
  ```
  python3 -m pip install --upgrade pip setuptools wheel
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
  version conflicts between multiple projects.
  - Create activate a virtual environment, activate it, and install dependencies.
  ```
  python -m venv env
  source env/bin/activate # env\Scripts\activate for windows
  pip install -r requirements.txt
  ```