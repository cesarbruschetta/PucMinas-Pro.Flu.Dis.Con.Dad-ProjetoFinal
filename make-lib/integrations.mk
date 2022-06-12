
integration-pipeline-local: poetry-check checks-nosave ## Runs all steps for integrating locally


poetry-check: safety ## Runs poetry check
	@poetry check

safety:
	@poetry run safety check --full-report -i 37894

docker-up: ## Starts all services on docker-compose as daemon
	@poetry run docker-compose up -d --force-recreate --build

docker-down: ## Stops all services on docker-compose
	@poetry run docker-compose down

docker-up-log: ## Starts all services on docker-compose as foreground
	@poetry run docker-compose up --force-recreate --build

docker-mongo: ## Starts mongo DB docker
	@poetry run docker-compose up -d --force-recreate --build mongo

docker-dependencies: docker-mongo ## Starts All docker dependencies

docker-apps-recreate:
	$(eval $(call check-var,APPS))
	@poetry run docker-compose up --force-recreate --build $(APPS)

wait:
	@sleep 20
