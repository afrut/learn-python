SHELL:=/bin/bash

define setup_environment
	set +a && \
	source ./envs/base.env && \
	source ./envs/derived.env && \
	set -a
endef

all: \
	install \
	create_project \
	create_venv \
	install_python_dependencies

install: \
	install_pipx \
	install_poetry

install_pipx:
	@$(setup_environment) && \
	sudo apt update && \
	sudo apt install pipx -y && \
	pipx ensurepath && \
	sudo pipx ensurepath --global # optional to allow pipx actions with --global argument

install_poetry:
	@$(setup_environment) && \
	pipx install poetry==$${POETRY_VERSION} && \
	poetry completions bash >> ~/.bash_completion

create_project:
	@$(setup_environment) && \
	poetry new $${PROJECT_TAG}

create_venv:
	@$(setup_environment) && \
	pyenv install --skip-existing $${PYTHON_VERSION} && \
	pyenv virtualenv $${PYTHON_VERSION} $${VENV_NAME} --force && \
	pyenv local $${VENV_NAME}

install_python_dependencies:
	@$(setup_environment) && \
	pip install -r "$${PROJECT_TAG}/requirements.txt"



lock:
	@$(setup_environment) && \
	PWD=$$(pwd) && \
	cd $${PROJECT_TAG} && \
	poetry lock && \
	poetry export --format requirements.txt --output requirements.txt --without-hashes

delete_venv:
	@$(setup_environment) && \
	pyenv uninstall --force $${VENV_NAME}