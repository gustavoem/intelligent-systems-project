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
        result = self.app_client.post("/v1/categorize", json=payload)
        categories = result.json
        self.assertTrue(len(categories) == 2)
        for category in categories:
            self.assertIn(category, KNWON_CATEGORIES)
