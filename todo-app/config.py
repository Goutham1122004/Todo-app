# config.py
import os

SECRET_KEY = os.urandom(24)
SQLALCHEMY_DATABASE_URI = 'sqlite:///todo.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False

KEYCLOAK_SERVER_URL = 'http://localhost:8080/auth/'
KEYCLOAK_CLIENT_ID = 'todo-app'
KEYCLOAK_REALM_NAME = 'your-realm'
KEYCLOAK_CLIENT_SECRET = 'your-client-secret'
