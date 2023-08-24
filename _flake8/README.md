# Background
- flake8 is a bundle of tools:
  - Pyflakes: checks Python source files for errors
  - pycodestyle: checks Python source files against style conventions
  - mccabe: checks McCabe complexity
- See (project page)[https://github.com/PyCQA/flake8]
- Installation
```
pyenv local 3.10.4
python -m venv env
source env/bin/activate
pip install flake8
```

# Usage
- Invoke via CLI
```
flake8 sample.py
```