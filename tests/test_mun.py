import unittest, os, shutil
from src.loader.mun import Mun
from testdata_generator import create_test_csv

class test_mun(unittest.TestCase):
    
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

    def test_insert_self(self):
        os.makedirs('tests/testdata/na')
        create_test_csv('tests/testdata/na/demo.csv')
        m = Mun('tests/testdata/na/demo.csv')
        self.assertEqual(len(m.insert_self()), 6)

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree('tests/testdata')

if __name__ == "__main__":
    unittest.main()