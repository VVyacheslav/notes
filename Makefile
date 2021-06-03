install-static-deps:
	npm install

build-static: install-static-deps
	npm run build

build-django:
	docker-compose build django

build: build-django

# Create superuser
create-superuser:
	docker-compose run django python manage.py create_admin

# Start web-server
runserver:
	docker-compose up -d

# Run tests
autotests:
	docker-compose run --rm django /app/start-autotests.sh

.PHONY: autotests runserver buld build-django create-superuser build-static install-static-deps
