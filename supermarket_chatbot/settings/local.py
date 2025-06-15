from pymongo import MongoClient
from .base import *  

DEBUG = True
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

client = MongoClient(MONGO_URI)
db = client[DB_NAME]
