# Load environment variables from .env
include .env
export $(shell sed 's/=.*//' .env)

SERVICE_NAME=app

build:
	docker-compose up --build -d

down:
	docker-compose down

up:
	docker-compose up -d

stop:
	docker-compose stop 

exec:
	docker-compose exec $(SERVICE_NAME) bash

migrate:
	docker-compose exec $(SERVICE_NAME) alembic upgrade head

migrate-new:
	docker-compose exec $(SERVICE_NAME) alembic revision --autogenerate -m "$(msg)"
