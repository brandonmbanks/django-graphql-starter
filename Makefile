# A lot of this is a straight rip-off from @jessfraz, because it's that awesome.

# Set an output prefix, which is the local directory if not specified
PREFIX?=$(shell pwd)

.PHONY: all
all: install env sleep db ## Fresh install and start the project. Run this by just typing 'make'.
	@echo "+ $@"
	@echo "Good to go 👍"

.PHONY: build
build: ## Build all of the project's containers.
	@echo "+ $@"
	@docker-compose build

.PHONY: clean
clean: stop ## Clean all of the project's containers and dependencies.
	@echo "+ $@"
	@docker-compose rm
	@rm -rf vendor

.PHONY: db
db: start ## Migrate the project's database.
	@echo "+ $@"
	@docker-compose exec app python manage.py migrate

.PHONY: env
env:
	@echo "+ $@"
	@cp .env.example .env

.PHONY: install
install: start ## Install the project's dependencies.
	@echo "+ $@"
	@docker-compose exec app pip install --user -r requirements.txt

.PHONY: lint
lint: start ## Lint project application's and test code.
	@echo "+ $@"
	@docker-compose exec app flake8

.PHONY: load
load: start ## Seed the project's database from fixtures.
	@echo "+ $@"
	@docker-compose exec app python manage.py loaddata **/fixtures/*.json

.PHONY: sleep
sleep:
	@echo "+ $@"
	@echo 'Waiting for the database to initialize... 😴'
	@sleep 10

.PHONY: start
start: ## Start all of the project's containers.
	@echo "+ $@"
	@docker-compose up -d

.PHONY: stop
stop: ## Stop all of the project's containers.
	@echo "+ $@"
	@docker-compose down

.PHONY: test
test: start ## Run the default tests for this project.
	@echo "+ $@"
	@docker-compose exec app pytest

.PHONY: update
update: ## Update the project's dependencies.
	@echo "+ $@"
	@docker run -it -v ${PREFIX}:/app ${COMPOSERIMAGE} update

.PHONY: help
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
