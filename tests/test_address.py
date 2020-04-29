import unittest
from src.models.address import address

insert_dict = {
        'housenumber': '123 A',
        'street': 'W Main St',
        'city': 'Vienna',
        'state': 'va',
        'zipcode': '22182'
    }

class test_address(unittest.TestCase):
    def test_inserting_into_database(self):
        a = address.from_dict(insert_dict)
        self.assertTrue(type(a.save()), int)

if __name__ == "__main__":


    unittest.main()