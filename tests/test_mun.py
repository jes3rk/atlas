import unittest, os, shutil
from src.loader.mun import Mun
from testdata_generator import create_test_csv, generate_csv_addresses

class test_mun(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        os.makedirs('tests/testdata/na')

    def test_parse_mun_name(self):
        options = [
            'city_of_mount_st_mary.csv',
            'vienna.csv',
            'town_of_apocolypse.csv',
            'eau_claire.csv',
            'new_york_city.csv'
        ]
        valid = [
            'Mount St Mary',
            'Vienna',
            'Apocolypse',
            'Eau Claire',
            'New York City'
        ]
        index = 0
        while index < len(options):
            self.assertEqual(valid[index], Mun.parse_mun_name(options[index]))
            index += 1

    def test_create_mun(self):
        file_path = 'data/us/ma/city_of_boston.csv'
        m = Mun(file_path)
        self.assertEqual(m.state, 'MA')
        self.assertEqual(m.mun_name, 'Boston')

    def test_valid_parse_addresses(self):
        create_test_csv('tests/testdata/na/demo.csv')
        m = Mun('tests/testdata/na/demo.csv')
        self.assertEqual(len(m.parse_addresses()), 1000)

    def test_invalid_parse_addresses(self):
        pass
    
    @classmethod
    def tearDownClass(cls):
        try:
            shutil.rmtree('tests/testdata')
        except:
            pass

if __name__ == "__main__":
    unittest.main()