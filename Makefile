SERVICE_NAME=app

build:
	docker-compose up --build -d

down:
	docker-compose down

up:
	docker-compose up -d

stop:
	docker-compose stop

run-foreground:
	docker-compose stop
	docker-compose up

re:
	docker-compose down
	docker-compose up --build -d

exec:
	docker-compose exec $(SERVICE_NAME) bash

migrate:
	docker-compose exec $(SERVICE_NAME) alembic revision --autogenerate -m "$(msg)"
	docker-compose exec $(SERVICE_NAME) alembic upgrade head

check:
	docker-compose exec $(SERVICE_NAME) pylint --disable=missing-docstring app/

format:
	docker-compose exec $(SERVICE_NAME) black .

mypy:
	docker-compose exec $(SERVICE_NAME) mypy --install-types app/

commit:
	git add -A
	git commit -m "$(msg)"
	git push



.PHONY: build down up stop run-foreground re exec migrate check format mypy commit
