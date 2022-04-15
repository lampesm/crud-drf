# How to run

first step install poetry:

`pip install poetry`

Then activate it 

`poetry shell` 

`poetry install`


## running with docker:


`docker build . -t crud-drf:1.0.0`

`docker-compose up`

----------------------

**paths:**

- http://127.0.0.1:8000/api/v1/create
- http://127.0.0.1:8000/api/v1/read
- http://127.0.0.1:8000/api/v1/update/{pk}
- http://127.0.0.1:8000/api/v1/delete/{pk}