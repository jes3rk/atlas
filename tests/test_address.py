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
        test_address.insert_id = a.insert()
        self.assertTrue(type(test_address.insert_id), int)

    def test_pulling_from_database(self):
        a = None
        if type(test_address.insert_id) is int:
            a = address.get({
                'id': test_address.insert_id
            })
        self.assertIsInstance(a, address)
    
    @classmethod
    def tearDownClass(cls):
        if type(test_address.insert_id) is int:
            address.delete({
                'id': test_address.insert_id
            })

if __name__ == "__main__":
    unittest.main()