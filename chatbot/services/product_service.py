from core.mongo_factory import MongoFactory
import logging
from chatbot.mongo_schemas.product_schema import product_schema


logger = logging.getLogger(__name__)

def get_all_products():
    '''permet de récupérer tous les produits de la collection MongoDB test'''
    mongo = MongoFactory.create('products')
    try:
        products = mongo.get_all_documents()
        logger.info(f"{len(products)} produits récupérés avec succès.")
        return products

    except Exception as e:
        logger.exception("Erreur lors de la récupération des produits")
        return None

    finally:
        mongo.close_connection()


def get_product_by_id(product_id):
    '''permet de récupérer un produit par son ID de la collection MongoDB test'''
    mongo = MongoFactory.create('products')
    try:
        product = mongo.get_document_by_id(product_id)
        if product:
            logger.info(f"Produit avec ID {product_id} récupéré avec succès.")
        else:
            logger.warning(f"Aucun produit trouvé avec l'ID {product_id}.")
        return product

    except Exception as e:
        logger.exception("Erreur lors de la récupération du produit par ID")
        return None

    finally:
        mongo.close_connection()


def get_products_by_pagination(page=1, limit=25):
    '''permet de récupérer les produits avec pagination'''
    mongo = MongoFactory.create('products')
    try:
        products = mongo.get_documents_with_pagination(page, limit)
        logger.info(f"{len(products)} produits récupérés pour la page {page} avec une limite de {limit}.")
        return products

    except Exception as e:
        logger.exception("Erreur lors de la récupération des produits avec pagination")
        return None

    finally:
        mongo.close_connection()

def get_products_by_category(category):
    '''permet de récupérer les produits par catégorie de la collection MongoDB test'''
    mongo = MongoFactory.create('products')
    try:
        filter_query = {"categorie": {"$regex": f"^{category}$", "$options": "i"}}
        products = mongo.get_sorted_documents(
            filter_query=filter_query,
            sort_field="nom",
            sort_order=1
        )
        if products:
            logger.info(f"{len(products)} produits récupérés pour la catégorie '{category}'.")
        else:
            logger.warning(f"Aucun produit trouvé pour la catégorie '{category}'.")
        return products
    except Exception as e:
        logger.exception("Erreur lors de la récupération des produits par catégorie")
        return None
    
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


def delete_product_by_id(product_id):
    '''Permet de supprimer un produit par son ID de la collection MongoDB test'''
    mongo = MongoFactory.create('products')
    try:
        result = mongo.delete_document_by_id(product_id)
        if result["deletedCount"] > 0:
            logger.info(f"Produit avec ID {product_id} supprimé avec succès.")
        else:
            logger.warning(f"Aucun produit trouvé avec l'ID {product_id}.")
        return result

    except Exception as e:
        logger.exception("Erreur lors de la suppression du produit par ID")
        return None

    finally:
        mongo.close_connection()


def update_product_by_id(product_id, update_data):
    '''Permet de mettre à jour un produit par son ID dans la collection MongoDB test'''
    mongo = MongoFactory.create('products')
    try:
        result = mongo.update_document_by_id(product_id, update_data)
        if result["modifiedCount"] > 0:
            logger.info(f"Produit avec ID {product_id} mis à jour avec succès.")
        else:
            logger.warning(f"Aucun produit trouvé avec l'ID {product_id} ou aucune modification apportée.")
        return result

    except Exception as e:
        logger.exception("Erreur lors de la mise à jour du produit par ID")
        return None

    finally:
        mongo.close_connection()