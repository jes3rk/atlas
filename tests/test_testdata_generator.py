import unittest
import testdata_generator
from src.models.address import _is_not_blank, _is_decimal, _is_valid_zip

class test_testdata_generator(unittest.TestCase):
    def test_0_generate_csv_addresses(self):
        import random
        count = random.randint(0, 100)
        l = testdata_generator.generate_csv_addresses(count)
        self.assertEqual(len(l), count)
    
    def test_stringify_csv_addresses(self):
        l = testdata_generator.generate_csv_addresses(1, True)[0]
        for e in l:
            self.assertEqual(type(e), str)

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