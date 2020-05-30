import unittest
import testdata_generator
from src.models.address import _is_not_blank, _is_decimal, _is_valid_zip

class test_testdata_generator(unittest.TestCase):

    def test_valid_format_valid_data_type_check(self):
        to_test = [
            {
                'vars': ['hello', 'world'],
                'type': str
            }, {
                'vars': [1, 2, 3, 4, 5, 6],
                'type': int
            }, {
                'vars': [1.234, 0.0384212398231],
                'type': float
            }, {
                'vars': [True, False],
                'type': bool
            }, {
                'vars': [[1, 2, 3, 4], ['hellld', 'jdjd'], [1.234, 'hello']],
                'type': list
            }, {
                'vars': [{
                    'hello': 'world'
                }], 
                'type': dict
            }
        ]
        self.assertTrue(testdata_generator._type_check(to_test))

    def test_invalid_data_type_check(self):
        to_test = [
            {
                'vars': [1, 'hello', True],
                'type': list
            }
        ]
        self.assertFalse(testdata_generator._type_check(to_test))

    def test_invalid_format_type(self):
        to_test = [
            ['hello'],
            'hello',
            {
                'vemmo': [1234]
            }
        ]
        self.assertRaises(TypeError, testdata_generator._type_check, to_test)

    def test_0_generate_csv_addresses(self):
        import random
        count = random.randint(0, 100)
        l = testdata_generator.generate_csv_addresses(count)
        self.assertEqual(len(l), count)

    def test_non_numeric_length_generate_csv_addresses(self):
        non_numerics = [
            True,
            False,
            None,
            'Hello World',
            [1, 2, 3], 
            {
                'hello': 'world'
            }
        ]
        for n in non_numerics:
            self.assertRaises(TypeError, lambda: testdata_generator.generate_csv_addresses(n))
    
    def test_non_boolean_props_generate_csv_addresses(self):
        non_bool = [
            None,
            'Hello World',
            [1, 2, 3],
            10.345,
            {
                'hello': 'world',
                '123': 123
            }
        ]
        for n in non_bool:
            self.assertRaises(TypeError, lambda: testdata_generator.generate_csv_addresses(100, stringify=n))
            self.assertRaises(TypeError, lambda: testdata_generator.generate_csv_addresses(100, lat=n))
            self.assertRaises(TypeError, lambda: testdata_generator.generate_csv_addresses(100, lon=n))
            self.assertRaises(TypeError, lambda: testdata_generator.generate_csv_addresses(100, number=n))
            self.assertRaises(TypeError, lambda: testdata_generator.generate_csv_addresses(100, street=n))
            self.assertRaises(TypeError, lambda: testdata_generator.generate_csv_addresses(100, city=n))
            self.assertRaises(TypeError, lambda: testdata_generator.generate_csv_addresses(100, postcode=n))


    def test_stringify_csv_addresses(self):
        l = testdata_generator.generate_csv_addresses(1, True)[0]
        for e in l:
            self.assertTrue(type(e) == str or e is None)

    def test_3_valid_generated_addresses(self):
        l = testdata_generator.generate_csv_addresses(1000)
        for addr in l:
            self.assertEqual(len(addr), 11)
            self.assertEqual(type(addr[0]), float)
            self.assertEqual(type(addr[1]), float)
            self.assertTrue(_is_not_blank(addr[2]))
            self.assertTrue(_is_not_blank(addr[3]))
            self.assertTrue(_is_not_blank(addr[5]))
            self.assertTrue(len(addr[8]) >= 5)
    
    def test_invalid_lat_lon_generated_addresses(self):
        l = testdata_generator.generate_csv_addresses(1000, lon=True, lat=True)
        for addr in l:
            self.assertEqual(len(addr), 11)
            self.assertFalse(_is_decimal(addr[0]))
            self.assertFalse(_is_decimal(addr[1]))

    def test_invalid_number_generated_addresses(self):
        l = testdata_generator.generate_csv_addresses(1000, number=True)
        for addr in l:
            self.assertEqual(len(addr), 11)
            self.assertFalse(_is_not_blank(addr[2]))

    def test_invalid_street_generated_addresses(self):
        l = testdata_generator.generate_csv_addresses(1000, street=True)
        for addr in l:
            self.assertEqual(len(addr), 11)
            self.assertFalse(_is_not_blank(addr[3]))
    
    def test_invalid_city_generated_addresses(self):
        l = testdata_generator.generate_csv_addresses(1000, city=True)
        for addr in l:
            self.assertEqual(len(addr), 11)
            self.assertFalse(_is_not_blank(addr[5]))

    def test_invalid_postcode_generated_addresses(self):
        l = testdata_generator.generate_csv_addresses(1000, postcode=True)
        for addr in l:
            self.assertEqual(len(addr), 11)
            self.assertFalse(_is_valid_zip(addr[8]))
            
if __name__ == "__main__":
    unittest.main()