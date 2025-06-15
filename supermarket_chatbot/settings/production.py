from .base import *
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path=BASE_DIR / 'env/.env.production')

DEBUG = False
ALLOWED_HOSTS = ['ton-domaine.com', 'www.ton-domaine.com']

# Connexion MongoDB production
from mongoengine import connect
connect(
    db=os.getenv("MONGO_DB_NAME"),
    host=os.getenv("MONGO_DB_HOST"),
    username=os.getenv("MONGO_DB_USER"),
    password=os.getenv("MONGO_DB_PASS"),
    authentication_source='admin'
)

# Sécurité production
SECURE_HSTS_SECONDS = 3600
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
