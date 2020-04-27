import unittest
from app import app

class testFlaskApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        self.assertEqual(app.debug, False)

    def tearDown(self):
        pass

    def test_home_route(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()