from product_service import *

initialize_product_collection()
produit1 = {
    "nom": "Pomme",
    "prix": 0.5,
    "description": "Pomme rouge délicieuse",
    "categorie": "Fruits"
}

produit2 = {
    "nom": "Pain",
    "prix": 1.0,
    "description": "Pain frais de la boulangerie",
    "categorie": "Boulangerie"
}

add_product(produit1)
add_product(produit2)