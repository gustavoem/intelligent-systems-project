from base_api_test import BaseAPITest
from constants import KNOWN_CATEGORIES

class CategorizerViewTest(BaseAPITest):

    def tests_categorizer_works(self):
        payload = {
            "products": [
                {"title": "brincos de ouro"},
                {"title": "mordedores para bebês"}
            ]
        }
        response = self.app_client.post("/v1/categorize", json=payload)
        categories = response.json.get("categories")
        self.assertTrue(len(categories) == 2)
        for category in categories:
            self.assertIn(category, KNOWN_CATEGORIES)


    def tests_bad_request_payloads(self):
        no_products_payload = {"products": []}
        response = self.app_client.post("v1/categorize",
                json=no_products_payload)
        self.assertTrue(response.status_code, 400)

        invalid_product_payload = {"products": [
            {"invalid_field": "crazy value"}
        ]}
        response = self.app_client.post("v1/categorize",
                json=no_products_payload)
        self.assertTrue(response.status_code, 400)

