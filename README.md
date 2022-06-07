# helloFlask
Projet POO

## Pyenv

### Show python versions accessible by pyenv on your PC
pyenv versions

### Show python versions available for install by pyenv
pyenv install --list

### Install python version
pyenv install 3.10.4

### Create virtualenv
pyenv virtualenv python_version env_name

### Activate environment
pyenv activate <env_name>

### List environments
pyenv virtualenvs

### Show python version used by default
pyenv --version

### Set default python version globally
pyenv global python_version

### Set default python version locally (one directory)
pyenv local python_version

## Poetry

### Initialize new project
poetry new package_name

### Add dependency
poetry add package_name

### Install project
poetry install

### Create build (whl and gz files)
poetry build
