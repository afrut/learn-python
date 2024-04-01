- *pipenv* is aimed at managing Python dependencies for projects with multiple
  collaborators.
  - Contributors can isolate a project's dependencies by creating
    virtual environments, installing dependencies, and `pip freeze >
    requirements.txt`. Other contributors can then activate their own virtual
    environments and `pip install -r requirements.txt`.
  - pipenv manages virtual environments and dependencies together.
- Install pipenv.
  ```
  pip install pipenv
  ```
- Install a package.
  ```
  pipenv install requests
  ```
- Run a script that uses the pipenv-installed package.
  ```
  pipenv run python main.py
  ```
- pipenv generates two files: *Pipfile* and *Pipfile.lock*.
  - More details for these files in (this link)[https://pipenv.pypa.io/en/latest/pipfile/].
- Other developers can use pipenv to install dependencies in these files. In the
  same directory as these files,
  ```
  pipenv install
  ```
- Start a shell session in the virtual environment that pipenv manages.
  ```
  pipenv shell
  ```
- Generate a requirements.txt.
  ```
  pipenv requirements
  ```