#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from dotenv import load_dotenv
from chatbot.services.product_service import add_product


load_dotenv()
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
    # Uncomment the line below to add a product to the database
    add_product("Test Product", "This is a test product", 9.99, "test_category")
    execute_from_command_line(sys.argv)
    

if __name__ == '__main__':
    main()
