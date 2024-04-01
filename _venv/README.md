# Background
- venv allows the isolation of pip dependencies by creating virtual environments.
- See (official documentation)[https://docs.python.org/3/library/venv.html].

# Usage
- Create a virtual environment in the directory *env*
```
python -m venv env
```
- Activate the environment
```
source env/bin/activate
```
- Install some dependencies
```
pip install requests pandas
```
- Install from requirements file
```
pip install -r requirements.txt
```
- Save installed packages to requirements file
```
pip freeze > requirements.txt
```