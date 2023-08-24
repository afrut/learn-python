Black is a code formatter for Python.
See their (project page)[https://github.com/psf/black].
- Activate a version of Python
  ```
  pyenv local 3.10.4
  ```
- Create venv and activate
  ```
  python -m venv env
  source env/bin/activate
  ```
- Install black
  ```
  pip install black
  pip freeze > requirements.txt
  ```
- Run test script for using black
  ```
  ./test_black.sh
  ```