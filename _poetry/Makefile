SHELL:=/bin/bash

define setup_environment
	set +a && \
	source ./envs/base.env && \
	source ./envs/derived.env && \
	set -a
endef

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

# create_venv:
# 	@$(setup_environment) && \
# 	echo $${FOO} && \
# 	pyenv install --skip-existing