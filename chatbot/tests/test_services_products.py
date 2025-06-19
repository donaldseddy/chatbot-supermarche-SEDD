from django.test import TestCase
from chatbot.services.product_service import *



from django.test import TestCase
from chatbot.services.product_service import *

class ProductServiceTests(TestCase):
    def setUp(self):
        # Donnée de test insérée avant chaque test
        self.product_data = {
            "nom": "Lait test",
            "prix": 1.99,
            "description": "Lait de test",
            "categorie": "Produits laitiers",
            "quantite": 20
        }
        inserted = add_product(self.product_data)
        self.inserted_id = str(inserted.inserted_ids[0])

    def tearDown(self):
        if hasattr(self, 'inserted_id'):
            delete_result = delete_product_by_id(self.inserted_id)
            self.assertIsNotNone(delete_result)
            self.assertTrue(delete_result["acknowledged"])
            self.assertEqual(delete_result["deletedCount"], 1)

            # Vérifie qu'il n'existe plus
            product = get_product_by_id(self.inserted_id)
            self.assertIsNone(product)


    def test_get_all_products(self):
        products = get_all_products()
        self.assertIsNotNone(products)
        self.assertIsInstance(products, list)

    def test_get_product_by_id(self):
        product = get_product_by_id(self.inserted_id)
        self.assertIsNotNone(product)
        self.assertEqual(str(product['_id']), self.inserted_id)

    def test_get_products_by_pagination(self):
        products = get_products_by_pagination(page=1, limit=10)
        self.assertIsNotNone(products)
        self.assertIsInstance(products, list)

    def test_get_products_by_category(self):
        category = "Produits laitiers"
        products = get_products_by_category(category)
        self.assertIsNotNone(products)
        self.assertIsInstance(products, list)
    

    def test_add_product(self):
        new_product = {
            "nom": "Fromage test",
            "prix": 2.99,
            "description": "Fromage de test",
            "categorie": "Produits laitiers",
            "quantite": 10
        }
        inserted = add_product(new_product)
        self.assertIsNotNone(inserted)
        self.assertTrue(isinstance(inserted.inserted_ids, list))
        self.assertEqual(len(inserted.inserted_ids), 1)

        # Vérifie que le produit a été ajouté
        product = get_product_by_id(str(inserted.inserted_ids[0]))
        self.assertIsNotNone(product)
        self.assertEqual(product['nom'], new_product['nom'])

    
    def test_delete_product_by_id(self):
        delete_result = delete_product_by_id(self.inserted_id)
        self.assertIsNotNone(delete_result)
        self.assertTrue(delete_result["acknowledged"])
        self.assertEqual(delete_result["deletedCount"], 1)

        # Vérifie qu'il n'existe plus
        product = get_product_by_id(self.inserted_id)
        self.assertIsNone(product)