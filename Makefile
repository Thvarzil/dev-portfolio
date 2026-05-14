COMPOSE = docker compose -f docker/docker-compose.yml

.PHONY: help dev up down logs shell migrate makemigrations createsuperuser collectstatic build

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "  %-20s %s\n", $$1, $$2}'

dev: ## Start backend container + frontend dev server
	$(COMPOSE) up -d
	@echo "Backend running at http://localhost:8000"
	@echo "Admin at http://localhost:8000/admin"
	@if [ -f frontend/portfolio/package.json ]; then \
		cd frontend/portfolio && npm run dev; \
	fi

up: ## Start containers in foreground
	$(COMPOSE) up

down: ## Stop containers
	$(COMPOSE) down

logs: ## Tail container logs
	$(COMPOSE) logs -f

shell: ## Open Django shell in running container
	$(COMPOSE) exec backend python manage.py shell

migrate: ## Run database migrations
	$(COMPOSE) exec backend python manage.py migrate

makemigrations: ## Create new migrations
	$(COMPOSE) exec backend python manage.py makemigrations

createsuperuser: ## Create a Django superuser
	$(COMPOSE) exec backend python manage.py createsuperuser

collectstatic: ## Collect static files
	$(COMPOSE) exec backend python manage.py collectstatic --noinput

build: ## Run production build script
	./scripts/build.sh
