import os
from dotenv import load_dotenv
from pymongo import MongoClient
from .base import *





load_dotenv(dotenv_path=BASE_DIR / 'env/.env.local')

DEBUG = True
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

MONGO_URI = os.getenv("MONGO_URI")
DB_NAME = os.getenv("DB_NAME")

client = MongoClient(MONGO_URI)
db = client[DB_NAME]

