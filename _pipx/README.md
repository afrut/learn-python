- Some packages provide tools that must be accessible globally via the command
  line. *pipx* creates virtual environments for these tools and makes sure they
  are accessible via the PATH variable.
  - Some useful ones are *black*, *flake8*, *mypy*, *isort*, and *pipenv*.
- Install pipx.
  ```
  pip install --user pipx
  ```
- Install the black package and update it.
  ```
  pipx install black
  pipx upgrade black
  ```
- Run the black command line tool using pipx. 
  ```
  pipx run black some_script.py
  ```
- See what is installed.
  ```
  pipx list
  ```