import sys
sys.path.insert (0, '..')

import unittest
from categorizer_service import get_categorizer
from constants import KNOWN_CATEGORIES


class CategorizerServiceTest(unittest.TestCase):

    def tests_categorizer_returns_a_known_category(self):
        categorizer = get_categorizer()
        sample_product = {
            "title": "carrinho relampago macqueen",
            "query": "carrinho de controle remoto",
            "concatenated_tags": "pixar carrinho brinquedo",
        }
        inferred_category = categorizer(sample_product)
        self.assertIn(inferred_category, KNOWN_CATEGORIES)

