from pymongo.collection import Collection
from pymongo.database import Database
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from bson import ObjectId
from jsonschema import validate, ValidationError


class MongoManager:
    def __init__(self, uri: str, db_name: str=None, coll_name: str=None):
        self.__client = MongoClient(uri, server_api=ServerApi('1'), tls=True)
        try:
            ping = self.__client.admin.command({'ping': 1})
            print(f"Pinged your deployment: {ping}. You successfully connected to MongoDB!")
        except Exception as e:
            raise Exception("Unable to connect to MongoDB due to the following error: ", e)
        self.__db = None
        self.__collection = None
        if db_name is not None:
            self.__db: Database = self.__client[db_name]
        if coll_name is not None:
            self.__collection: Collection = self.__db[coll_name]
    
    def close_connection(self):
            self.__client.close()
            print("Connection closed.")

    @property
    def db(self) -> Database:
        if self.__db is None:
            raise Exception("Database not initialized. Please provide a database name.")
        return self.__db
    
    @db.setter
    def db(self, db_name: str):
        self.__db = self.__client[db_name]
    # réaffectation obligatoire de la collection car changement de database
        if self.__collection is not None:
            self.collection = self.__collection.name # .name car collection est un objet

    @property
    def collection(self) -> Collection:
        if self.__collection is None:
            raise Exception("Collection not initialized. Please provide a collection name.")
        return self.__collection
    
    @collection.setter
    def collection(self, coll_name: str):
        if self.__db is None:
            raise Exception("Database not initialized. Please provide a database name.")
        self.__collection = self.__db[coll_name]
        print(f"Collection set to '{coll_name}'")


    def list_databases(self):
        try:
            return self.__client.list_database_names()
        except Exception as e:
            raise Exception("Unable to list databases due to the following error: ", e)
    

    def create_collection(self, coll_name: str, schema: dict = None):
        if self.__db is None:
            raise Exception("Database not initialized. Please provide a database name.")
        
        if coll_name in self.__db.list_collection_names():
            print(f"La collection '{coll_name}' existe déjà. Aucune création nécessaire.")
            self.__collection = self.__db[coll_name]
            return self.__collection

        try:
            if schema:
                self.__collection = self.__db.create_collection(
                    coll_name,
                    validator={"$jsonSchema": schema}
                )
            else:
                self.__collection = self.__db.create_collection(coll_name)

            print(f"Collection '{coll_name}' créée avec succès.")
            return self.__collection

        except Exception as e:
            raise Exception(f"Impossible de créer la collection à cause de l'erreur suivante : {e}")


            
    def list_collections(self):
        if self.__db is None:
            raise Exception("Database not initialized. Please provide a database name.")
        try:
            return self.__db.list_collection_names()
        except Exception as e:
            raise Exception("Unable to list collections due to the following error: ", e)
        


    def create_one_document(self, document, schema: dict = None):
        if self.__collection is None:
            raise Exception("Collection not initialized. Please provide a collection name.")
        if schema:
            try:
                validate(instance=document, schema=schema)
            except ValidationError as e:
                raise Exception(f"Document validation failed: {e.message}")
        try:
            result = self.__collection.insert_one(document)
            return result.inserted_id
        except Exception as e:
            raise Exception("Unable to create document due to the following error: ", e)
        

    def create_many_documents(self, documents, schema: dict = None):
        if self.__collection is None:
            raise Exception("Collection not initialized. Please provide a collection name.")
        if schema:
            for document in documents:
                try:
                    validate(instance=document, schema=schema)
                except ValidationError as e:
                    raise Exception(f"Document validation failed: {e.message}")
        try:
            result = self.__collection.insert_many(documents)
            return result.inserted_ids
        except Exception as e:
            raise Exception("Unable to create documents due to the following error: ", e)
        
        
    def update_document_by_id(self, id, new_values: dict):
        """
        Met à jour un document via son identifiant (_id).
        :param id: str ou ObjectId – l'identifiant MongoDB du document à mettre à jour
        :param new_values: dict – les nouvelles valeurs à mettre à jour dans le document
        :return: dict – le résultat de la mise à jour
        """
        if self.__collection is None:
            raise Exception("Collection not initialized. Please provide a collection name.")
        
        try:
            object_id = ObjectId(id) if not isinstance(id, ObjectId) else id
            update_result = self.collection.update_one({"_id": object_id}, {"$set": new_values})
            return {
                "acknowledged": update_result.acknowledged,
                "matchedCount": update_result.matched_count,
                "modifiedCount": update_result.modified_count,
            }
        except Exception as e:
            raise Exception("Unable to update the document due to the following error:", e)
    

    def update_many_documents(self, query: dict, new_values: dict):
        try:
            update_result = self.collection.update_many(query, new_values)
            return {
            "acknowledged": update_result.acknowledged,
            "insertedId": update_result.upserted_id,
            "matchedCount": update_result.matched_count,
            "modifiedCount": update_result.modified_count,
            }
        except Exception as e:
            raise Exception("Unable to update the documents due to the following error:", e)
        

    def get_all_documents(self):
        try:
            documents = self.collection.find()
            return list(documents)
        except Exception as e:
            raise Exception("Unable to retrieve all documents due to the following error:", e)
        
    
    def get_document_by_id(self, id):
        """
        Récupère un document via son identifiant (_id).
        :param id: str ou ObjectId – l'identifiant MongoDB du document à récupérer
        :return: dict – le document trouvé ou None si non trouvé
        """
        try:
            object_id = ObjectId(id) if not isinstance(id, ObjectId) else id
            document = self.collection.find_one({"_id": object_id})
            return document
        except Exception as e:
            raise Exception("Unable to retrieve the document due to the following error:", e)
        


    def get_documents_with_pagination(self, page: int = 1, limit: int = 25):
        """
        Récupère les documents avec pagination.
        :param page: int – numéro de la page (1-indexé)
        :param limit: int – nombre de documents par page
        :return: list de documents
        """
        if page < 1 or limit < 1:
            raise ValueError("Page and limit must be greater than 0.")
        
        try:
            skip = (page - 1) * limit
            documents = self.collection.find().skip(skip).limit(limit)
            return list(documents)
        except Exception as e:
            raise Exception("Unable to retrieve documents with pagination due to the following error:", e)
        

        
    def get_sorted_documents(self, query: dict, sort_by: str, order: int):
        try:
            documents = self.collection.find(query).sort(sort_by, order)
            return list(documents)
        except Exception as e:
            raise Exception("Unable to read the sorted documents due to the following error:", e)
        

    

    def delete_document_by_id(self, id):
        """
        Supprime un document via son identifiant (_id).
        :param id: str ou ObjectId – l'identifiant MongoDB du document à supprimer
        :return: dict – le résultat de la suppression
        """
        try:
            object_id = ObjectId(id) if not isinstance(id, ObjectId) else id
            delete_result = self.collection.delete_one({"_id": object_id})
            return {
                "acknowledged": delete_result.acknowledged,
                "deletedCount": delete_result.deleted_count,
            }
        except Exception as e:
            raise Exception("Unable to delete the document due to the following error:", e)
        
    
    def delete_many_documents(self, query: dict):
        try:
            delete_result = self.collection.delete_many(query)
            return {
            "acknowledged": delete_result.acknowledged,
            "deletedCount": delete_result.deleted_count,
            }
        except Exception as e:
            raise Exception("Unable to delete the documents due to the following error:", e)
        
   
    def get_documents_from_collection(self, collection_name):
        """
        Récupère tous les documents d'une collection spécifiée dynamiquement.
        :param collection_name: str - le nom de la collection MongoDB
        :return: list de documents
        """
        if not collection_name:
            raise ValueError("Collection name must be provided.")
        
        try:
            collection = self.__db[collection_name]
            documents = list(collection.find())

            # Convertir les ObjectId en chaînes pour JSON
            for doc in documents:
                if '_id' in doc:
                    doc['_id'] = str(doc['_id'])

            return documents

        except Exception as e:
            raise RuntimeError(f"Unable to retrieve documents from collection '{collection_name}': {e}")
        

    
