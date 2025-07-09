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
        self.inserted_id = str(inserted) 


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
        self.assertGreater(len(products), 0)  # Vérifie qu'il y a des produits

    def test_get_products_by_category(self):
        category = "Produits laitiers"

        # Optionnel : afficher le produit inséré pour vérifier
        product = get_product_by_id(self.inserted_id)
        print("Produit inséré :", product)

        products = get_products_by_category(category)
        print(f"Produits trouvés pour la catégorie '{category}':", products)

        self.assertIsNotNone(products, "La fonction a retourné None au lieu d'une liste")
        self.assertIsInstance(products, list, "La fonction ne retourne pas une liste")
        self.assertGreater(len(products), 0, "Aucun produit trouvé dans la catégorie")

    

    def test_add_product(self):
        new_product = {
            "nom": "Fromage test",
            "prix": 2.99,
            "description": "Fromage de test",
            "categorie": "Produits laitiers",
            "quantite": 10
        }
        inserted_id = add_product(new_product)  # ObjectId directement
        self.assertIsNotNone(inserted_id)

        # Vérifie que le produit a été ajouté
        product = get_product_by_id(str(inserted_id))
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


    def test_search_products(self):
        query = "Lait"
        products = search_products(query)
        self.assertIsNotNone(products)
        self.assertIsInstance(products, list)
        self.assertGreater(len(products), 0)