# core/mongo_factory.py
from supermarket_chatbot.settings.base import MONGO_URI, DB_NAME
from core.mongo_manager import MongoManager
from django.conf import settings

class MongoFactory:
    @staticmethod
    def create(collection_name: str = None) -> MongoManager:
        return MongoManager(
            uri=MONGO_URI,
            db_name=DB_NAME,
            coll_name=collection_name
        )