import unittest
from src.models.address import address

class test_address(unittest.TestCase):
    def test_inserting_into_database(self):
        a = address.from_dict({
            'housenumber': '123',
            'street': 'W Main St',
            'city': 'Vienna',
            'state': 'va',
            'zipcode': '22182'
        })
        a.save()

if __name__ == "__main__":
    unittest.main()