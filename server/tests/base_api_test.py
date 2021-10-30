import sys
sys.path.insert(0, '..')

import unittest
from api import create_app

def app_client():
    app = create_app(is_testing=True)
    return app.test_client()


class BaseAPITest(unittest.TestCase):

    def setUp(self):
        self.app_client = app_client()

