.DEFAULT_GOAL := help

COMPOSE_DEV = docker compose -f compose.yml -f compose.dev.yml
COMPOSE_PROD = docker compose -f compose.yml

.PHONY: help deps build pull up up-dev down setup deploy

help:
	@echo "Usage:"
	@echo "  make logs    		- Check Docker container logs"
	@echo "  make deps    		- Build frontend assets"
	@echo "  make test    		- Make test container, run tests, down test container"
	@echo "  make build   		- Build Docker images"
	@echo "  make build-force   - Build Docker images"
	@echo "  make pull    		- Pull Docker images"
	@echo "  make up      		- Start production environment"
	@echo "  make up-dev  		- Start development environment"
	@echo "  make down    		- Stop and remove containers, networks, images, and volumes"
	@echo "  make setup   		- Setup server with dependencies and clone repo"
	@echo "  make deploy  		- Deploy site onto server"
	@echo "  make cypress-start	- Start Cypress"
	@echo ""

logs:
	docker compose logs -f

deps:
	uv pip install
	yarn install
	yarn run build

build:
	$(COMPOSE_DEV) build api db

build-force:
	$(COMPOSE_DEV) build --no-cache api db

pull:
	docker compose pull

up:
	$(COMPOSE_PROD) up -d --force-recreate

up-dev:
	$(COMPOSE_DEV) up -d --force-recreate api db

down:
	$(COMPOSE_DEV) down
	$(COMPOSE_PROD) down

build-ci:
	docker compose -f compose.yml -f compose.dev.yml build

up-ci:
	docker compose -f compose.yml -f compose.dev.yml up -d --force-recreate

test:
	$(COMPOSE_DEV) up -d test-db  
	$(COMPOSE_DEV) run --rm test 
	$(COMPOSE_DEV) down
