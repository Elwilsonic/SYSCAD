import unittest
from app import create_app
from app.schemas import ResponseSchema

class HomeResourceTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_index(self):
        response_schema = ResponseSchema()
        response = self.client.get('/api/v1/')
        self.assertEqual(response.status_code, 200)
        message = response_schema.load(response.get_json())
        self.assertEqual(message["message"], response.get_json()["message"])
        self.assertEqual(message["data"], response.get_json()["data"])

if __name__ == '__main__':
    unittest.main()
