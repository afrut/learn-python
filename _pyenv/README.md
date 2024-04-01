# Background
- pyenv allows easy switching between Python versions.
- It is useful for testing applications and programs for compatibility between
different versions.
- See the (project page)[https://github.com/pyenv/pyenv].

# Usage
- List all available version of Python available for installation
```
pyenv install -l
```
- See how `pyenv install` resolves a *prefix*
```
pyenv latest -k prefix
```
- See how `pyenv *other_command*` resolves a *prefix*
```
pyenv latest prefix
```
- Install Python 3.10.4
```
pyenv install 3.10.4
```
- Use Python 3.10.4 globally
```
pyenv global 3.10.4
```
- Use Python 3.10.4 in the current shell session
```
pyenv shell 3.10.4
```
- Use Python 3.10.4 whenever you are in the current directory or its
subdirectories. This command creates a file `.python-version` in the current
directory.
```
pyenv local 3.10.4
```
- See currently active version
```
pyenv version
```
- See all versions
```
pyenv versions
```
- Uninstall 3.10.4
```
pyenv uninstall 3.10.4
```