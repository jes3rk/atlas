import unittest
from src.models.address import address
from testdata_generator import generate_valid_csv_addresses

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

    def test_valid_address_from_csv(self):
        raw_data = generate_valid_csv_addresses()[0] ## this should change when I make true random valid generator
        self.assertEqual(address.from_csv(raw_data).is_valid, True)
    
    @classmethod
    def tearDownClass(cls):
        try:
            if type(test_address.insert_id) is int:
                address.delete({
                    'id': test_address.insert_id
                })
        except:
            pass

if __name__ == "__main__":
    unittest.main()