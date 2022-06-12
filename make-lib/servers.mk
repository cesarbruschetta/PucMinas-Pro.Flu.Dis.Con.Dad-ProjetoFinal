
serve-local: ## Serve application locally
	@echo "###\nStarting Django server...\n###\n"
	@poetry run cog_platform/manage.py runserver 0.0.0.0:${PORT}

up-local-servers:
	@echo "Starting local servers"
	@poetry run coverage run -p -- cog_platform/manage.py runserver &

down-local-servers:
	@echo "Stoping local servers"
	@-(ps aux | awk '/cog_platform/ {print $$2}' | xargs kill -SIGTERM)
	@sleep 2
