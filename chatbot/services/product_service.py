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

def get_product_by_id(product_id):
    mongo = MongoFactory.create(product_schema)

    try:
        product = mongo.read_one_document({"_id": product_id})
        if product:
            logger.info(f"Produit trouvé: {product['name']}")
            return product
        else:
            logger.warning(f"Aucun produit trouvé avec l'ID: {product_id}")
            return None

    except Exception as e:
        logger.exception("Erreur lors de la récupération du produit")
        return None

    finally:
        mongo.close_connection()


def add_product(product_data):
    mongo = MongoFactory.create('products')

    try:
        result = mongo.create_collection(product_data, product_schema)
        if result:
            logger.info(f"Produit ajouté avec succès: {product_data['nom']}")
            return result
        else:
            logger.error("Échec de l'ajout du produit")
            return None
    except Exception as e:
        logger.exception("Erreur lors de l'ajout du produit")
        return None
    

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


