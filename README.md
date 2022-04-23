# Simple CRUD - Django REST Framework with MySQL and Docker

[Django REST Framework](https://www.django-rest-framework.org/) is a powerful web framework for building API.

In this project, you will learn how to build methods [GET, PUT, POST, DELETE] by **DRF** and how to connect it to **MySQL** and finally **dockerized** the project.


## Requirements
- docker
- docker-compose

## Use

`cp .env.example .env` and replace your environment in .env file

then build your api and running other command until your container is ready 

`docker-compose build`

`docker-compose up`

`docker-compose run api python manage.py migrate `

----------------------

**end points:**

- http://127.0.0.1:8000/api/v1/create
- http://127.0.0.1:8000/api/v1/read
- http://127.0.0.1:8000/api/v1/update/{pk}
- http://127.0.0.1:8000/api/v1/delete/{pk}

<br>

## License

[GNU](https://github.com/lampesm/crud-drf/blob/main/LICENSE)