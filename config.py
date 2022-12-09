from os import environ

APP_HOST = environ.get("APP_HOST")
DOG_API_URL = f'{APP_HOST}/api'
STATUS_CODE_SUCCESS = 200
