#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from dotenv import load_dotenv
from chatbot.services.product_service import *
from chatbot.services.fontions_exo import product_list
from supermarket_chatbot.settings.base import MONGO_URI, DB_NAME


load_dotenv()
import os
import sys
from chatbot.services.product_service import add_product  # Assure-toi que l'import est correct

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'supermarket_chatbot.settings.base')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    # ✅ Ajoute le produit une seule fois en évitant la double exécution de Django
    if os.environ.get('RUN_MAIN') == 'true':
        add_product({
            "nom": "Lait demi-écrémé",
            "prix": 1.15,
            "description": "Bouteille de lait 1L demi-écrémé",
            "categorie": "Produits laitiers",
            "quantite": 50
        })
        add_product(product_list)
    
    main()
