import unittest
from src.models.address import address

class test_address(unittest.TestCase):

    insert_dict = {
            'housenumber': '123',
            'street': 'W Main St',
            'city': 'Vienna',
            'state': 'va',
            'zipcode': '22182'
        }
    def test_inserting_into_database(self):
        a = address.from_dict(self.insert_dict)
        self.assertEqual(a.save(), True)
    
    def test_retrival(self):
        a = address.get()

if __name__ == "__main__":
    unittest.main()