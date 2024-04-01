- Using `pip freeze > requirements.txt` to manage dependencies is not enough.
  Sometimes, a dependency's underlying package dependencies can break another
  package. It is a good idea to pin ALL package dependencies.
- Pin the versions of all package dependencies listed in *requirements.in*.
  - Generates *requirements.txt*.
  - Use the `--output_file other_file.txt` to re-direct to another file.
  ```
  pip-compile requirements.in
  ```
- Install the required packages.
  ```
  pip install -r requirements.txt
  ```