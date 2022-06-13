
serve-local: ## Serve application locally
	@echo "###\nStarting Django server...\n###\n"
	@poetry run python ./api/main.py

build-recommendations: ## Build recommendations
	@echo "###\nBuilding recommendations...\n###\n"
	@poetry run python ./processing/generation_of_recommendations.py
