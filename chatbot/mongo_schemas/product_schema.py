# chatbot/mongo_schemas/product_schema.py
product_schema = {
    "bsonType": "object",
    "required": ["nom", "prix", "description", "categorie"],
    "properties": {
        "nom": {"bsonType": "string", "description": "Nom du produit"},
        "prix": {"bsonType": "double", "description": "Prix du produit"},
        "description": {"bsonType": "string", "description": "Description du produit"},
        "categorie": {"bsonType": "string", "description": "Catégorie du produit"}
    }
}