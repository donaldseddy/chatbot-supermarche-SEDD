"""
Django settings for supermarket_chatbot project.
"""

import os
from pathlib import Path
from decouple import Config, RepositoryEnv

# Définir le chemin de base du projet
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Définir le bon fichier .env selon l'environnement DJANGO_SETTINGS_MODULE
if os.getenv('DJANGO_SETTINGS_MODULE') == 'supermarket_chatbot.settings.local':
    env_file = BASE_DIR / 'env' / '.env.local'
else:
    env_file = BASE_DIR / 'env' / '.env.production'

# Charger les variables d'environnement depuis le bon fichier
try:
    config = Config(RepositoryEnv(str(env_file)))
except FileNotFoundError:
    raise FileNotFoundError(f"Fichier .env introuvable à : {env_file}")

# Variables MongoDB
MONGO_URI = config.get('MONGO_URI')
DB_NAME = config.get('DB_NAME')

# Django secret key
SECRET_KEY = config.get('SECRET_KEY', default='django-insecure-placeholder')

# Debug mode
DEBUG = config.get('DEBUG', default=False, cast=bool)

# Liste d'hôtes autorisés
ALLOWED_HOSTS = config.get('ALLOWED_HOSTS', default='localhost,127.0.0.1').split(',')

# Applications installées
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',

    # Apps perso
    'chatbot'
]

# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

# Configuration des templates
ROOT_URLCONF = 'supermarket_chatbot.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Application WSGI
WSGI_APPLICATION = 'supermarket_chatbot.wsgi.application'

# Base de données (par défaut SQLite)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Validation des mots de passe
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalisation
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Fichiers statiques
STATIC_URL = 'static/'

# Clé primaire par défaut
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,

    'formatters': {
        'verbose': {
            'format': '[{asctime}] {levelname} {name} - {message}',
            'style': '{',
        },
    },

    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': BASE_DIR / 'logs' / 'app.log',
            'formatter': 'verbose',
        },
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
    },

    'loggers': {
        'django': {
            'handlers': ['file', 'console'],
            'level': 'INFO',
            'propagate': True,
        },
        'chatbot': {
            'handlers': ['file', 'console'],
            'level': 'DEBUG',
            'propagate': False,
        },
    },
}


CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
]