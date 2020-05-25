import unittest
from src.models.address import address, _is_not_blank, _is_decimal, _is_valid_zip
from testdata_generator import generate_csv_addresses

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
        raw_data = generate_csv_addresses(1000, stringify=True)
        for addr in raw_data:
            self.assertTrue(address.from_csv(addr, 'NA').is_valid)

    def test_missing_city_from_csv(self):
        import random
        l = list()
        while len(l) < 1000:
            if random.random() < .5:
                l.extend(generate_csv_addresses(1, True))
            else:
                l.extend(generate_csv_addresses(1, True, city=True))
        for addr in l:
            self.assertTrue(address.from_csv(addr,'NA', city='Valid City').is_valid)
    
    def test_eliminate_statewide(self):
        l = generate_csv_addresses(1000, True, city=True)
        for addr in l:
            self.assertFalse(address.from_csv(addr, 'NA', city='statewide').is_valid)

    def test_is_blank(self):
        self.assertTrue(_is_not_blank('hello world'))
        self.assertTrue(_is_not_blank(str(18.2836029123)))
        self.assertFalse(_is_not_blank(None))
        self.assertFalse(_is_not_blank(""))

    def test_is_decimal(self):
        self.assertFalse(_is_decimal('hello world'))
        self.assertTrue(_is_decimal(str(18.2836029123)))
        self.assertTrue(_is_decimal(str(120)))
        self.assertFalse(_is_decimal(None))
        self.assertFalse(_is_decimal(""))
    
    def test_is_valid_zip(self):
        tries = [
            ['22180', True],
            ['22182-0392', True],
            ['1234', False],
            ['abscd', False],
            [12344, False],
            [12, False],
            [True, False],
            ['12sk4', False],
            ['1239x-fdk2', False]
        ]
        for t in tries:
            print('Testing {t}'.format(t=t[0]))
            self.assertEqual(_is_valid_zip(t[0]), t[1])

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