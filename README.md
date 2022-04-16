# Simple CRUD - Django REST Framework with MySQL database and Docker

Django REST framework is a powerful web framework for building API 


----------------------
## Requirements
- Docker
- docker-compose

------------------
## Use

create **root** user and **database** in mysql with following command

`docker build . -t mysql-db:1.0.0 -f mysql/Dockerfile`

then build your api and running other command until your container is ready 

`docker-compose build`

`docker-compose up`

`docker exec -it crud-drf-container bash` then `python manage.py migrate sessions`

----------------------

**paths:**

- http://127.0.0.1:8000/api/v1/create
- http://127.0.0.1:8000/api/v1/read
- http://127.0.0.1:8000/api/v1/update/{pk}
- http://127.0.0.1:8000/api/v1/delete/{pk}

<br>

## License

[MIT] https://github.com/esmail-ebrahimi/crud-drf/blob/main/LICENSE