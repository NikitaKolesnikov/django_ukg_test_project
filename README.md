# django_ukg_test_project
To work and test this project you need to install docker and docker-compose on your machine.
Also, to speed up your work you can use "make" commands described in Makefile.


### Common projects commands with `make`

1) build project `make build`
2) run migrations `make migrations`
3) run project `make up`
4) stop project `make stop`
5) run tests `make test` (Works with stopped ukg_restaurant container)
6) run type checks `make typecheck` (Works with running ukg_restaurant container)
7) run linter checks `make lint` (Works with running ukg_restaurant container)

### Common project projects with `docker-compose`

1) build project `docker-compose build`
2) run migrations `docker-compose run ukg_restaurant pipenv run python manage.py migrate`
3) run project `docker-compose up`
4) stop project `docker-compose stop`
5) run tests `docker-compose run ukg_restaurant pipenv run python manage.py test`


### API Documentation is available in 2 different styles, to reach you can follow:
1) http://0.0.0.0:8000/api-docs/redoc/
2) http://0.0.0.0:8000/api-docs/swagger/
