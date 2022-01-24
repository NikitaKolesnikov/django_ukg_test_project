APP_NAME='ukg_restaurant'
PROJECT_DIRECTORY_NAME='src'
DCET = docker-compose exec ${APP_NAME}
PROJECT_PY_FILES=`find . -type f -regex "^.*.py" -not -path "*/migrations/*" -not -path "*/src/*" -not -path "*manage.py"`
ENV_RUN = pipenv run

.PHONY: build
build:
	@#@ build docker image
	@docker-compose  build
	@echo Done build

.PHONY: up
up:
	@#@ Run docker-compose up
	@docker-compose up
	@echo Done up


.PHONY: stop
stop:
	@docker-compose stop
	@echo Done stop

.PHONY: shell
shell:
	@docker-compose run ${APP_NAME} ${ENV_RUN} python manage.py shell

.PHONY: shell
shell:
	@docker-compose run ${APP_NAME} ${ENV_RUN} python manage.py s

.PHONY: down
down:
	@docker-compose down -v
	@echo Done down

.PHONY: restart
restart:
	@docker-compose restart
	@echo Done full restart

.PHONY: restart-service
restart-service:
	@docker-compose restart ${APP_NAME}
	@echo Done ${APP_NAME} restart

.PHONY: typecheck
typecheck:
	@#@ Run typechecking using mypy inside VM or prepared environment from the project root.
	@${DCET} ${ENV_RUN} mypy --ignore-missing-imports --config-file=conf/mypy.ini $(PROJECT_PY_FILES)
	@echo Done typecheck

.PHONE: build-for-test
build-for-test:
	@docker-compose -f docker-compose-test.yml build
	@docker-compose -f docker-compose-test.yml run ${APP_NAME} pipenv run python manage.py migrate

.PHONY: test
test:
	@docker-compose -f docker-compose-test.yml up ${APP_NAME}
	@docker-compose -f docker-compose-test.yml stop db-test

.PHONE: test-one
test-one:
	@docker-compose -f docker-compose-test.yml run ${APP_NAME} pipenv run python manage.py test $$APP
	@docker-compose -f docker-compose-test.yml stop db-test

.PHONY: lint
lint:
	@#@ Runs linter inside VM or prepared environment from the project root.
	@${DCET} pipenv run pylint --load-plugins pylint_quotes --rcfile=conf/.pylintrc $(PROJECT_PY_FILES) -d duplicate-code tests/
	@echo Done lint

.PHONY: migrations
migrations:
	@docker-compose run ${APP_NAME} pipenv run python manage.py makemigrations
	@echo Done

.PHONY: migrate
migrate:
	@docker-compose run ${APP_NAME} pipenv run python manage.py migrate
	@echo Done

.PHONY: bash
bash:
	@#@  log into container shell
	@docker-compose exec ${APP_NAME} sh

.PHONY: pre-commit-check
pre-commit-check:
	@#@ Run all checks before commit except tests
	@echo Linter check
	@make lint
	@echo Type check
	@make typecheck
	@echo Pre-commit checks
	@pre-commit run --all-files

.PHONY: run-with-ports
run-with-ports:
	@# Run main service with service ports
	@docker-compose run --service-ports ${APP_NAME}
