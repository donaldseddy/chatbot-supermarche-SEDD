from core.mongo_factory import MongoFactory
import logging
from chatbot.mongo_schemas.product_schema import product_schema


logger = logging.getLogger(__name__)

def get_all_products():
    mongo = MongoFactory.create('products')

    try:
        products = mongo.read_many_documents({})
        count = len(products)
        logger.info(f"{count} produits trouvés dans MongoDB.")
        return products

    except Exception as e:
        logger.exception("Erreur lors de la récupération des produits")
        return []

    finally:
        mongo.close_connection()




def add_product(product_data):
    '''permet d'ajouter un produit à la collection MongoDB test si cest une liste de dictionnaires ou un seul dictionnaire'''
    mongo = MongoFactory.create('products')
    try:
        if isinstance(product_data, list):
            result = mongo.create_many_documents(product_data)
            logger.info(f"{len(result)} produits ajoutés avec succès.")
        else:
            result = mongo.create_one_document(product_data)
            logger.info("Produit ajouté avec succès.")
        return result

    except Exception as e:
        logger.exception("Erreur lors de l'ajout du produit")
        return None

    finally:
        mongo.close_connection()
    

def initialize_product_collection():
    """
    Initialise la collection de produits dans MongoDB.
    Cette fonction est appelée au démarrage de l'application pour s'assurer que la collection existe.
    """
    mongo = MongoFactory.create('products')

    try:
        mongo.create_collection('products', product_schema)
        logger.info("Collection de produits initialisée avec succès.")
    except Exception as e:
        logger.exception("Erreur lors de l'initialisation de la collection de produits")
    finally:
        mongo.close_connection()


