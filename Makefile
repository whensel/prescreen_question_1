-include .env.$(or $(APP_ENV),dev)
export

.PHONY: test
test: ## Runs the tests
	poetry run pytest -v

.PHONY: lint
lint: ## Runs the linters
	poetry run black --check .

.PHONY: fmt
fmt: ## Runs the formatters
	poetry run black .

.PHONY: startapp
startapp: ## Installs dependencies
	python -m pip install --upgrade pip
	pip install poetry
	poetry install

.PHONY: help
help: ## Display this message
	@grep -h -E '^[a-zA-Z0-9\._-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
# .DEFAULT_GOAL := help