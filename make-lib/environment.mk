install-poetry: ## Installs poetry as user
	@pip install poetry --user

dependencies: ## Installs dev dependencies
	@poetry install --no-root

shell: ## Open an ipython on poetry
	@poetry run ipython

lock: ## Update Locks Pipfile.lock
	@poetry lock
