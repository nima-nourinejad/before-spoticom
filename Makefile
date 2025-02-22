SERVICE_NAME=app
MSG_MIGRATION=new migration
MSG_GIT=update

build:
	docker-compose up --build -d

down:
	docker-compose down

up:
	docker-compose up -d

stop:
	docker-compose stop

re:
	docker-compose down
	docker-compose up --build -d

exec:
	docker-compose exec $(SERVICE_NAME) bash

migrate:
	docker-compose exec $(SERVICE_NAME) alembic upgrade head

migrate-new:
	docker-compose exec $(SERVICE_NAME) alembic revision --autogenerate -m "$(MSG_MIGRATION)"

check:
	docker-compose exec $(SERVICE_NAME) pylint --disable=missing-docstring app/

format:
	docker-compose exec $(SERVICE_NAME) black .

mypy:
	docker-compose exec $(SERVICE_NAME) mypy app/

git:
	git add -A
	git commit -m "$(MSG_GIT)"
	git push

.PHONY: build down up stop re exec migrate migrate-new check format mypy git
