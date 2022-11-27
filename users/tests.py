from rest_framework.test import APITestCase
from .views import get_random, get_access_token, get_refresh_token

class TestGenericFunctions(APITestCase):

    def test_get_random(self):
        
        rand1 = get_random(10)
        rand2 = get_random(10)
        rand3 = get_random(15)

        self.assertTrue(rand1)

        self.assertNotEqual(rand1, rand2)

        self.assertEqual(len(rand1), 10)
        self.assertEqual(len(rand3), 15)
    
    def test_get_access_token(self):
        payload = {
            "id": 1
        }

        token = get_access_token(payload)

        self.assertTrue(token)
    
    def test_get_refresh_token(self):
        token = get_refresh_token()

        self.assertTrue(token)