# Installation

`python3 -m venv venv`

`source venv/bin/activate`

`pip install -r requirements.txt`

## Database

Install & run mysql

Create `chats_scheduler` db

### Set db env variables
`export DB_USER=<user>`
`export DB_PASSWORD=<password>`

## Redis
Install & run redis

# Run

### Populate DB
`python manage.py loaddata data.json`

### Start Django
`python manage.py runserver`

### Start Celery
`celery -A chatscheduler worker -l INFO`

# API

### Get a token:
`python manage.py drf_create_token admin`

### Headers
`Authorization: Token <token>`

### Get chat
`GET http://127.0.0.1:8000/chats/<id>`

### Create chat
`POST http://127.0.0.1:8000/chats/<id>`

Params: user_id, discount_id, conversation_id, payload

### Get conversation
`GET http://127.0.0.1:8000/conversations/<id>`

### Get chat
`POST http://127.0.0.1:8000/conversations/<id>`

Params: client_id, operator_id, store_id